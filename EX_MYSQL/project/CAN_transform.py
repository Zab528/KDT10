def make_can_data(start_bit: int, bit_length: int, raw_value: int) -> str:
    """
    start_bit, bit_length, raw_value(0~(2^bit_length-1))를 받아서
    8바이트 CAN DATA를 '00 00 00 00 00 00 00 00' 형태의 문자열로 반환.
    """
    # 1) 값 범위 체크 (예: bit_length=2면 raw_value는 0~3)
    max_val = (1 << bit_length) - 1
    if not (0 <= raw_value <= max_val):
        raise ValueError(f"raw_value는 0~{max_val} 사이여야 합니다.")

    # 2) 64비트(8바이트) 정수 초기값 0
    all_bits = 0

    # 3) 해당 구간에 raw_value 세팅
    #    - bit_length만큼 마스크 만든 다음
    #    - start_bit 위치에 raw_value를 밀어 넣기
    all_bits |= (raw_value & max_val) << start_bit

    # 4) 64비트를 8바이트 little-endian으로 변환
    data_bytes = all_bits.to_bytes(8, byteorder="little")

    # 5) '00 00 00 00 00 00 00 00' 형태의 문자열로 변환
    hex_str = " ".join(f"{b:02X}" for b in data_bytes)
    return hex_str


# 예시 테스트
if __name__ == "__main__":
    # 1비트짜리 (예: 헤드램프 Low, start_bit=31, raw_value=1)
    print(make_can_data(31, 1, 1))   # → '00 00 00 80 00 00 00 00'

    # 2비트짜리 (예: C_VolUpSW: 24|2, raw_value=3(=11b))
    print(make_can_data(24, 2, 3))   # → '00 00 00 03 00 00 00 00'

    # 3비트짜리 (예: C_IGNSW: 12|3, raw_value=7(=111b))
    print(make_can_data(12, 3, 7))   # → '00 70 00 00 00 00 00 00'