def make_can_data(start_bit: int, bit_length: int) -> str:
    """
    start_bit, bit_length를 받아서
    해당 비트 구간을 모두 1로 세팅한 8바이트 CAN DATA를
    '00 00 00 00 00 00 00 00' 형태의 문자열로 반환.
    """
    if bit_length <= 0 or bit_length > 64:
        raise ValueError("bit_length는 1~64 사이여야 합니다.")

    # bit_length만큼 1로 채운 값 (예: bit_length=3 → 0b111 = 7)
    value = (1 << bit_length) - 1

    # 64비트 값 전체에서 start_bit 위치로 shift
    bits = value << start_bit

    # 64비트 정수를 8바이트 little-endian으로 변환
    data_bytes = bits.to_bytes(8, byteorder="little")

    # 사람이 보기 좋은 hex 문자열로 변환
    hex_str = " ".join(f"{b:02X}" for b in data_bytes)
    return hex_str


# ------------ 테스트 예시 ------------
if __name__ == "__main__":
    # 예1) start_bit=31, bit_length=1  → bit31만 1
    print("31,1 →", make_can_data(31, 1))  # 00 00 00 80 00 00 00 00

    # 예2) start_bit=24, bit_length=2  → bit24~25 = 11b
    print("24,2 →", make_can_data(24, 2))  # 00 00 00 03 00 00 00 00

    # 예3) start_bit=12, bit_length=3  → bit12~14 = 111b
    print("12,3 →", make_can_data(12, 3))  # 00 70 00 00 00 00 00 00

    # 예4) 네가 말한 (25,3) 테스트
    print("25,3 →", make_can_data(25, 3))  # 00 00 00 1C 00 00 00 00 이런 식으로 나올 거야