import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
from io import BytesIO
import json
import mysql.connector   # ✅ DB 접속용

# ================================
# DB 연결 함수 (네 환경에 맞게 수정)
# ================================
def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="user1",
        password="user1",   # ← 너 비번
        database="car_skill",      # ← 실제 DB 이름
    )

# ================================
# DBC 한 줄에서 신호 이름 뽑기
#   예: 'SG_ CF_Tmu_VehSld : 0|1@1+ ...'
#   → 'CF_Tmu_VehSld'
# ================================
def extract_signal_name(original_code: str) -> str:
    s = original_code.strip()
    if s.startswith("SG_"):
        s = s[3:].lstrip()
    # ':' 또는 공백 전까지를 이름으로 사용
    for sep in [":", " "]:
        idx = s.find(sep)
        if idx != -1:
            return s[:idx]
    return s   # 안전용

# ================================
# 신호 이름으로 CAN ID / start_bit / bit_length 조회
#   signals_info.name = 신호이름
#   messages.id       = signals_info.message_id
#   messages.frame_id = CAN ID
# ================================
def get_signal_info(signal_name: str):
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT 
            m.frame_id AS can_id,
            s.start_bit,
            s.bit_length
        FROM signals_info AS s
        JOIN messages AS m
          ON s.message_id = m.id
        WHERE s.name = %s
        LIMIT 1;
    """
    cur.execute(query, (signal_name,))
    row = cur.fetchone()

    cur.close()
    conn.close()
    return row  # 없으면 None


# ==================================================================
# UI 설정
# ==================================================================
st.set_page_config(layout="wide")


# ============================================
# 클래스 정의 (CarPoint)
# ============================================
class CarPoint:
    def __init__(self, id, name, start_bit, bit_length, factor, offset, x, y):
        self.id = id  # 점 ID / 식별자
        self.name = name  # 신호 이름
        self.start_bit = start_bit
        self.bit_length = bit_length
        self.factor = factor
        self.offset = offset

        self.x = x  # 화면에서 점 위치
        self.y = y

    def to_dict(self):
        return self.__dict__


# ============================================
# 이미지 → base64 변환
# ============================================
def load_image_base64(path):
    img = Image.open(path)
    buf = BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode()
    return img.size[0], img.size[1], b64


orig_w, orig_h, car_base64 = load_image_base64("car.png")


# ============================================
# CSS (padding 없애고 컬럼 제대로 배치)
# ============================================
st.markdown(
    """
<style>
/* 전체 좌우 레이아웃 여백 */
.block-container {
    padding-top: 20px;
    padding-left: 130px;
    padding-right: 30px;
    margin-top: 10px;
}

/* 실행, 로그 버튼 스타일 */
.stButton > button {
    width: 140px;
    height: 40px;
    background-color: #f7eaea;
    border-radius: 7px;
    border: 1px solid #ccc;
    font-size: 16px;
}

/* 버튼 사이 간격 */
.stButton {
    margin-top: 27px;
    margin-right: 10px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================
# 가로 6:4 로 나누기
# ============================================
left_col, right_col = st.columns([6, 4])

# --------------------------------------------
# 왼쪽 CAN UI
# --------------------------------------------
with left_col:
    st.markdown("## ~ CAN 통신 해석 ~")

    # selectbox + 실행 & 로그 버튼 가로 배치
    with st.container():
        colA, colB, colC = st.columns([4, 1, 1])

        with colA:
            search_value = st.text_input("CAN 통신값 검색", placeholder="original_code 한 줄 붙여넣기")

        with colB:
            exec_btn = st.button("해석")

        with colC:
            log_btn = st.button("로그")

    # ================================
    # 버튼 클릭 시, DBC 풀네임 → 신호 이름 → DB 조회
    # ================================
    if exec_btn and search_value:
        # 1) original_code 한 줄에서 신호 이름 추출
        signal_name = extract_signal_name(search_value)

        # 2) DB에서 CAN ID / start_bit / bit_length 조회
        info = get_signal_info(signal_name)

        # 결과 출력용 placeholder
        can_id_placeholder = st.empty()
        empty_space = st.empty()
        empty_space.markdown(
            """
            <div style="width: 100%; height: 2px;"></div>
            """,
            unsafe_allow_html=True,
        )
        bit_placeholder = st.empty()

        if info:
            can_id = info["can_id"]
            start_bit = info["start_bit"]
            bit_length = info["bit_length"]

            # CAN ID 출력
            can_id_placeholder.markdown(
                f"""
                <div style="
                    width: 100%;
                    height: 40px;
                    padding: 10px;
                    font-size: 16px;
                    background-color: #f0f0f0;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                    color: #333;
                ">
                    CAN ID: {can_id}
                </div>
                """,
                unsafe_allow_html=True,
            )

            # BIT 정보 출력 (start_bit | bit_length)
            bit_placeholder.markdown(
                f"""
                <div style="
                    width: 100%;
                    height: 40px;
                    padding: 10px;
                    font-size: 16px;
                    background-color: #f0f0f0;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                    color: #333;
                ">
                    BIT: {start_bit} | {bit_length}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.warning(
                f"'{signal_name}' 에 해당하는 신호를 찾지 못했습니다.\n"
                "signals_info.name 이랑 original_code 내용이 맞는지 확인해보세요."
            )

    # 여백 + 아래 박스 두 개 (기존 그대로)
    st.markdown("<hr><br>", unsafe_allow_html=True)

    col1, col2 = st.columns([6, 4])

    db_result_1 = "DB에서 가져온 결과 1"  # for col1
    db_result_2 = "DB에서 가져온 결과 2"  # for col2

    with col1:
        st.markdown(
            f"""
        <div style="
            width: 100%;
            height: 200px;
            background-color: #f7eaea;
            border-radius: 12px;
            padding: 20px;
            font-size: 18px;
            color: #333;
        ">
        {db_result_1}
        </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div style="
            width: 100%;
            height: 200px;
            background-color: #e0e0e0;
            border-radius: 12px;
            padding: 20px;
            font-size: 18px;
            color: #333;
        ">
            {db_result_2}
        </div>
        """,
            unsafe_allow_html=True,
        )

# --------------------------------------------
# 오른쪽 자동차 캔버스
# --------------------------------------------
with right_col:
    x = orig_w // 2 + 15
    # 점 8개 생성 (예시)
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
