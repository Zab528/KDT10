# can_gui.py
import streamlit as st
from dataclasses import dataclass

st.set_page_config(page_title="CAN 해석기", page_icon="🚗", layout="centered")

# ------------------------------
# 데이터베이스(임시) - 나중에 CSV로 빼면 됨
# ------------------------------
@dataclass
class SignalDef:
    can_id: int
    name: str
    start_bit: int
    length: int
    scale: float
    offset: float
    meaning: dict  # raw → text

SIGNALS = [
    SignalDef(
        can_id=1345,
        name="CF_Gway_HeadLampLow",
        start_bit=31,
        length=1,
        scale=1.0,
        offset=0.0,
        meaning={0: "OFF", 1: "ON"},
    ),
    SignalDef(
        can_id=1345,
        name="CF_Gway_HeadLampHigh",
        start_bit=32,
        length=1,
        scale=1.0,
        offset=0.0,
        meaning={0: "OFF", 1: "ON"},
    ),
]


# ------------------------------
# 파싱 로직
# ------------------------------
def parse_hex_to_int(data_str: str) -> int:
    """'00 00 00 80 00 00 00 00' → 64bit 정수"""
    byte_list = [int(b, 16) for b in data_str.split()]
    if len(byte_list) != 8:
        raise ValueError("CAN DATA는 8바이트여야 합니다.")
    return int.from_bytes(byte_list, byteorder="little")


def extract_raw(value: int, start_bit: int, length: int) -> int:
    mask = (1 << length) - 1
    return (value >> start_bit) & mask


def decode_can(can_id: int, data_str: str):
    all_bits = parse_hex_to_int(data_str)
    result = {}

    for sig in SIGNALS:
        if sig.can_id != can_id:
            continue

        raw = extract_raw(all_bits, sig.start_bit, sig.length)
        physical = raw * sig.scale + sig.offset
        text = sig.meaning.get(raw, str(physical))

        result[sig.name] = {
            "raw": raw,
            "physical": physical,
            "text": text
        }
    return result


# ------------------------------
# GUI
# ------------------------------
st.title("🚗 CAN 신호 자동 해석기 (프로토타입)")
st.write("임시 DB(신호 2개) 기반 – Low / High Beam 상태 해석 데모")

can_id = st.text_input("CAN ID (예: 1345)", value="1345")
data_str = st.text_input("CAN DATA (8바이트 Hex, 예: 00 00 00 80 00 00 00 00)",
                         value="00 00 00 00 00 00 00 00")

if st.button("해석하기"):
    try:
        cid = int(can_id)
        result = decode_can(cid, data_str)

        st.subheader("🔍 해석 결과")

        if len(result) == 0:
            st.warning("해당 CAN ID에 정의된 신호가 없습니다.")
        else:
            for name, info in result.items():
                st.write(f"**{name}** → {info['text']} (raw={info['raw']})")

            # 한 줄 요약
            low = result.get("CF_Gway_HeadLampLow", {}).get("raw")
            high = result.get("CF_Gway_HeadLampHigh", {}).get("raw")

            st.subheader("📌 상태 요약")
            if low == 1 and high == 0:
                st.success("현재 **Low Beam(로우빔)** 켜짐")
            elif low == 0 and high == 1:
                st.success("현재 **High Beam(하이빔)** 켜짐")
            elif low == 0 and high == 0:
                st.info("전조등 OFF")
            else:
                st.error("특이 상태 (Low/High 둘 다 1)")
    except Exception as e:
        st.error(f"오류: {e}")
