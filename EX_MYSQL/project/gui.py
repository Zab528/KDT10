import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
from io import BytesIO
import json
import pandas as pd
import re
from sqlalchemy import create_engine

## ==================================================================
## 데이터베이스 및 분석 로직 함수 정의
## ==================================================================

def run_db_analysis():
    """
    DB에서 데이터를 가져와 분석한 뒤, 텍스트 리포트를 반환하는 함수
    """
    lines = [] # 결과 텍스트를 저장할 리스트

    try:
        # 1. DB 연결 (사용자 환경에 맞춰 설정)
        engine = create_engine("mysql+pymysql://root:iopl321@localhost:3306/car_skill")
        sql = "SELECT * FROM signals"
        df_all = pd.read_sql(sql, engine)
        engine.dispose()

        lines.append(f"✅ 전체 데이터 로드 완료: {len(df_all)}건\n")

        # 2. 카테고리 및 패턴 정의
        category_patterns = {
            "헤드램프": r"(?i)HeadLamp|HLamp|H_Lamp|Low.*Beam|High.*Beam|AFLS|HBA|AHB|HLow|HHigh|PassingSW|ALight",
            "안전벨트": r"(?i)SeatBelt|Bkl|SBR|PSB|BeltCmd",
            "문": r"(?i)Door|DrSw|Dr.*Stat|Dr.*Open",
            "창문": r"(?i)Wdw|Window|Glass",
            "후미등": r"(?i)Tail|Rear.*Fog|License|StopLamp|HMSL|BrakeLight",
            "트렁크": r"(?i)Trunk|TailGate|Boot",
            "엑셀": r"(?i)Accel|Pedal|APS|Throttle|AclAct",
            "브레이크": r"(?i)Brake|Brk|ABS|ESS|EPB|AVH",
            "썬루프": r"(?i)SunRoof|Roof",
            "공조장치_HVAC": r"(?i)Temp|Aircon|Blower|Defrost|FATC|DATC|Heater|Climat",
            "핸들_조향": r"(?i)Steer|StrAng|MDPS|SAS|Torque|Handwhl",
            "타이어_TPMS": r"(?i)TPMS|Pressure|Tire|Psi",
            "주행보조_ADAS": r"(?i)SCC|Lkas|Ldws|Fcw|HDA|Cruise|Lane|Assist",
            "와이퍼": r"(?i)Wiper|Rain|Washer",
            "주차보조": r"(?i)AVM|PAS|Parking"
        }

        normal_pattern = r"(?i)Stat|Sw$|Switch|Value$|Option|Cmd|Enable|Req|Mode"
        error_pattern = r"(?i)Fail|Error|Open|OpenSts|Short|Fault|Warning|Wrn|Abnormal|Diag"

        # 3. 분류 로직 적용
        def classify_signal(name):
            category = "기타(미분류)"
            for cat, pat in category_patterns.items():
                if re.search(pat, name):
                    category = cat
                    break
            
            status = "일반"
            if re.search(error_pattern, name):
                status = "고장(Error)"
            elif re.search(normal_pattern, name):
                status = "작동(Status)"
            
            return pd.Series([category, status])

        df_all[['Category', 'Status']] = df_all['name'].apply(classify_signal)

        # 4. 리포트 생성
        lines.append("=" * 40)
        lines.append(f"{'부품별 상세 분석 리포트':^40}")
        lines.append("=" * 40)

        for category in category_patterns.keys():
            df_cat = df_all[df_all['Category'] == category]
            if df_cat.empty:
                continue

            df_error = df_cat[df_cat['Status'] == "고장(Error)"]
            df_normal = df_cat[df_cat['Status'] == "작동(Status)"]
            
            lines.append(f"\n[{category}]")
            lines.append(f"  - 전체 신호 : {len(df_cat)}건")
            lines.append(f"  - 고장 신호 : {len(df_error)}건")
            lines.append(f"  - 작동 신호 : {len(df_normal)}건")
            
            if not df_error.empty:
                lines.append(f"  ⚠️ 고장 샘플 : {df_error['name'].head(3).tolist()}")
            if not df_normal.empty:
                lines.append(f"  ✅ 작동 샘플 : {df_normal['name'].head(3).tolist()}")
            
            lines.append("-" * 40)

        # 미분류 데이터
        df_etc = df_all[df_all['Category'] == "기타(미분류)"]
        lines.append(f"\n[기타(미분류)] - 총 {len(df_etc)}건")
        if not df_etc.empty:
            lines.append(f"  ❓ 샘플 : {df_etc['name'].head(5).tolist()}")

    except Exception as e:
        lines.append(f"❌ DB 연결 또는 분석 중 오류 발생:\n{str(e)}")
        # 테스트를 위해 에러 발생 시에도 가짜 데이터를 보여주고 싶다면 여기서 처리 가능

    return "\n".join(lines)


## ==================================================================
## UI 시작
## ==================================================================
st.set_page_config(layout="wide")

# ... (CarPoint 클래스 및 이미지 로드 코드는 그대로 유지) ...
class CarPoint:
    def __init__(self, id, name, start_bit, bit_length, factor, offset, x, y):
        self.id = id
        self.name = name
        self.start_bit = start_bit
        self.bit_length = bit_length
        self.factor = factor
        self.offset = offset
        self.x = x
        self.y = y
    def to_dict(self):
        return self.__dict__

def load_image_base64(path):
    try:
        img = Image.open(path)
        buf = BytesIO()
        img.save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode()
        return img.size[0], img.size[1], b64
    except:
        # 이미지가 없을 경우를 대비해 더미 데이터 반환
        return 800, 600, ""

# 이미지 경로가 정확한지 확인해주세요
orig_w, orig_h, car_base64 = load_image_base64("car.png")


# ============================================
# CSS
# ============================================
st.markdown(
    """
<style>
.block-container {
    padding-top: 20px;
    padding-left: 50px; /* 레이아웃 조정 */
    padding-right: 30px;
    margin-top: 10px;
}
.stButton > button {
    width: 100%; /* 버튼 너비 꽉 차게 */
    height: 40px;
    background-color: #f7eaea;
    border-radius: 7px;
    border: 1px solid #ccc;
    font-size: 16px;
}
/* 결과 박스 내부 스크롤바 스타일 */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: #888; 
    border-radius: 4px;
}
</style>
""",
    unsafe_allow_html=True,
)

left_col, right_col = st.columns([6, 4])

# --------------------------------------------
# 왼쪽 CAN UI
# --------------------------------------------
with left_col:
    st.markdown("## ~ CAN 통신 해석 ~")

    with st.container():
        colA, colB, colC = st.columns([4, 1, 1])
        with colA:
            search_value = st.text_input("CAN 통신값 검색", placeholder="검색어 입력")
        with colB:
            exec_btn = st.button("해석")
        with colC:
            log_btn = st.button("로그")

    # ----------------------------------
    # 버튼 로직 처리
    # ----------------------------------
    # 결과 변수 초기화
    db_result_1 = "검색 결과 대기 중..."
    db_result_2 = "해석 버튼을 누르면\n전체 부품 분석 리포트가\n이곳에 표시됩니다."

    # 해석 버튼 클릭 시 로직
    if exec_btn:
        # 1. 검색어 처리 (기존 로직)
        db_results_mock = {
            "fgfg": {"CAN ID": 1532, "BIT": 10},
            "abc": {"CAN ID": 2048, "BIT": 15},
            "xyz": {"CAN ID": 1024, "BIT": 7},
        }
        
        if search_value:
            result = db_results_mock.get(search_value, None)
            if result:
                db_result_1 = f"검색 성공!\nCAN ID: {result['CAN ID']}\nBIT: {result['BIT']}"
            else:
                db_result_1 = f"'{search_value}'에 대한 검색 결과가 없습니다."
        
        # 2. DB 전체 분석 리포트 실행 (새로 추가한 로직)
        with st.spinner("데이터베이스 분석 중..."):
            db_result_2 = run_db_analysis()

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    # ===================================
    # 결과창 2개 배치
    # ===================================
    res_col1, res_col2 = st.columns([1, 1]) # 5:5 비율로 보기 좋게 조정

    # 왼쪽 결과창 (검색 결과)
    with res_col1:
        st.markdown(f"""
        <div style="
            width: 100%;
            height: 400px;
            background-color: #f7eaea;
            border-radius: 12px;
            padding: 20px;
            font-size: 16px;
            color: #333;
            overflow-y: auto; /* 내용 넘치면 스크롤 */
            white-space: pre-wrap; /* 줄바꿈 유지 */
        ">
        <strong>[검색 결과]</strong><br><br>
        {db_result_1}
        </div>
            """,
            unsafe_allow_html=True,
        )

    # 오른쪽 결과창 (DB 분석 리포트 - 여기가 핵심!!)
    with res_col2:
        st.markdown(f"""
        <div style="
            width: 100%;
            height: 400px;
            background-color: #e0e0e0;
            border-radius: 12px;
            padding: 20px;
            font-size: 14px; /* 리포트가 기니까 폰트 약간 작게 */
            color: #333;
            overflow-y: auto; /* 내용 넘치면 스크롤 (필수) */
            white-space: pre-wrap; /* 줄바꿈(\n)을 HTML <br>처럼 처리 (필수) */
            font-family: monospace; /* 리포트 느낌 나게 등폭 폰트 사용 */
        ">
        <strong>[시스템 분석 리포트]</strong><br><br>
        {db_result_2}
        </div>
        """,
            unsafe_allow_html=True,
        )

# --------------------------------------------
# 오른쪽 자동차 캔버스
# --------------------------------------------
with right_col:
    # (기존 코드와 동일)
    x = orig_w // 2 + 15
    points = [
        CarPoint("front_bumper", "SCC_ObjDist", 32, 16, 0.1, 0, x, 120),
        CarPoint("bonnet", "ENG_RPM", 8, 16, 1, 0, x, 200),
        CarPoint("windshield_left", "LDWS_LnStr", 12, 8, 1, 0, x - 100, 150),
        CarPoint("windshield_right", "HBA_LAMP", 20, 1, 1, 0, x + 100, 150),
        CarPoint("roof", "GPS_Lat", 0, 32, 0.0001, 0, x, 40),
        CarPoint("rear_glass", "RVM_STATUS", 16, 8, 1, 0, x, 450),
        CarPoint("right_door", "DOOR_STATUS_FR", 4, 2, 1, 0, x, 300),
        CarPoint("trunk", "POS_RR_W_LAMP", 48, 1, 1, 0, x, 550),
    ]
    points_json = json.dumps([p.to_dict() for p in points])
    
    canvas_html = f"""
    <canvas id="carCanvas" width="{orig_w}" height="{orig_h}"
            style="
                border:none;
                background-image:url('data:image/png;base64,{car_base64}'); 
                background-size:100% 100%;
                background-repeat:no-repeat;
                background-position:center;
            ">
    </canvas>
    <script>
    let points = {points_json};
    let c = document.getElementById("carCanvas");
    let ctx = c.getContext("2d");
    function drawPoints() {{
        ctx.clearRect(0, 0, c.width, c.height);
        points.forEach(p => {{
            ctx.beginPath();
            ctx.arc(p.x, p.y, 10, 0, 2*Math.PI);
            ctx.fillStyle = p.color || "red";
            ctx.fill();
            // 텍스트 라벨 추가
            ctx.fillStyle = "black";
            ctx.font = "12px Arial";
            ctx.fillText(p.name, p.x + 12, p.y + 4);
        }});
    }}
    c.addEventListener("click", (e) => {{
        const rect = c.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        points.forEach(p => {{
            if (Math.hypot(p.x - x, p.y - y) < 30) {{
                p.color = (p.color === "red") ? "green" : "red";
            }}
        }});
        drawPoints();
    }});
    drawPoints();
    </script>
    """
    components.html(canvas_html, height=orig_h + 20)