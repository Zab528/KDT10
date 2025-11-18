import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
from io import BytesIO
import json
import mysql.connector   # ✅ DB 접속용

# ================================
# DB 연결 함수 (값 너 환경에 맞게)
# ================================
def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="비밀번호",
        database="dbc_db",   # 실제 DB 이름으로 변경
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
# signals_info.name = 신호이름
# messages.id = signals_info.message_id
# messages.frame_id = CAN ID
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
