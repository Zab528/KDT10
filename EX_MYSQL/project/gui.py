import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
from io import BytesIO
import json

# ✅ MySQL 연결 라이브러리
import mysql.connector


# ================================
# DB 연결 함수 (네 환경에 맞게 수정)
# ================================
def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="비밀번호",
        database="dbc_db",   # 네가 만든 DBC용 DB 이름
    )

# ================================
# 1) 신호 이름으로 CAN ID + 비트 정보 가져오기
# ================================
def get_signal_info(signal_name: str):
    """
    signals_info.name = signal_name 인 행을 찾고
    messages.frame_id (CAN ID), start_bit, bit_length를 가져옴
    """
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
# 2) (start_bit, bit_length) → 8바이트 DATA 만들기
# ================================
def make_can_data(start_bit: int, bit_length: int) -> str:
    """
    start_bit, bit_length를 받아서
    해당 구간을 모두 1로 채운 64비트 값을 만든 뒤
    '00 00 00 00 00 00 00 00' 형태의 문자열로 반환
    """
    if bit_length <= 0 or bit_length > 64:
        raise ValueError("bit_length는 1~64 사이여야 합니다.")

    value = (1 << bit_length) - 1    # bit_length=3 → 0b111
    bits = value << start_bit        # 해당 위치로 시프트

    data_bytes = bits.to_bytes(8, byteorder="little")
    return " ".join(f"{b:02X}" for b in data_bytes)

    # ================================
    # 버튼 클릭 시, DB에서 신호 정보 조회
    # ================================
    if exec_btn and search_value:
        signal_name = search_value.strip()  # 앞뒤 공백 제거

        # 1) DB에서 CAN ID, start_bit, bit_length 가져오기
        info = get_signal_info(signal_name)

        # 2) 결과 표시용 placeholder 미리 만들기
        can_id_placeholder = st.empty()
        empty_space = st.empty()
        empty_space.markdown(
            """
            <div style="width: 100%; height: 2px;"></div>
            """,
            unsafe_allow_html=True,
        )
        bit_placeholder = st.empty()
        data_placeholder = st.empty()

        # 3) 결과가 있을 때
        if info:
            can_id = info["can_id"]
            start_bit = info["start_bit"]
            bit_length = info["bit_length"]

            # 8바이트 DATA 자동 생성 (해당 비트 구간을 모두 1로)
            try:
                data_hex = make_can_data(start_bit, bit_length)
            except Exception as e:
                data_hex = f"데이터 생성 오류: {e}"

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

            # 8바이트 DATA 출력
            data_placeholder.markdown(
                f"""
                <div style="
                    width: 100%;
                    height: 40px;
                    padding: 10px;
                    font-size: 16px;
                    background-color: #f7eaea;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                    color: #333;
                    margin-top: 5px;
                ">
                    DATA: {data_hex}
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:
            st.warning("검색 결과가 없습니다. signals_info.name 값을 다시 확인해주세요.")
