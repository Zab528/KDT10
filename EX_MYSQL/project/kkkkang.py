import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# ============================================
# DB 연결 함수
# ============================================
def get_conn():
    try:
        conn = mysql.connector.connect(
            host="172.30.1.87",
            user="user1",
            password="user1",
            database="car_skill",
            port=3306,
            connection_timeout=5,
        )
        return conn
    except Error as e:
        messagebox.showerror("DB 접속 에러", f"DB에 접속할 수 없습니다.\n\n{e}")
        return None

# ============================================
# original_code 문자열에서 start_bit, bit_length 파싱
# 예: 'SG_ SAS_Angle : 0|16@little_endian 0.1 0.0 Deg'
# → start_bit = 0, bit_length = 16
# ============================================
def parse_bits_from_original_code(original_code: str):
    try:
        # ':' 뒤쪽
        after_colon = original_code.split(":", 1)[1].strip()
        # '@' 앞까지만 사용 → '0|16'
        before_at = after_colon.split("@", 1)[0].strip()
        start_str, length_str = before_at.split("|")
        return int(start_str), int(length_str)
    except Exception as e:
        print("[DEBUG] parse_bits 실패:", original_code, e)
        return None, None

# ============================================
# Intel(@1) 기준 비트 마스크 계산
# - start_bit: LSB 기준 0번 비트부터 시작
# - bit_length: 사용하는 비트 개수
# 결과: 8바이트(64비트) 마스크
#   예: start_bit=2, bit_length=1 → 0x04 00 00 00 00 00 00 00
# ============================================
def calculate_bits(start_bit: int, bit_length: int):
    total_bits = [0] * 8  # 8바이트 = 64비트

    if start_bit is None or bit_length is None:
        return total_bits

    for i in range(bit_length):
        bit_position = start_bit + i      # 전체 비트 위치 (0~63)
        if bit_position >= 64:
            break

        byte_index = bit_position // 8    # 몇 번째 바이트인지
        bit_index = bit_position % 8      # 그 바이트 안에서 몇 번째 비트인지 (LSB = 0)

        # LSB가 0번 비트이므로 그대로 shift
        total_bits[byte_index] |= (1 << bit_index)

    return total_bits

# ============================================
# original_code 문자열로 CAN ID 조회
#   original_code 테이블에서 해당 줄 찾고
#   → message_id → messages.frame_id
# ============================================
def get_can_id_by_original_code(original_code: str):
    conn = get_conn()
    if conn is None:
        return None

    try:
        cur = conn.cursor(dictionary=True)

        # 공백 제거해서 정확 매칭 시도
        clean = original_code.strip()
        print("[DEBUG] original_code 파라미터:", repr(clean))

        query1 = """
            SELECT message_id, original_code
            FROM original_code
            WHERE TRIM(original_code) = TRIM(%s)
            LIMIT 1;
        """
        cur.execute(query1, (clean,))
        row = cur.fetchone()

        # 정확 매칭 안 되면 LIKE 로 한 번 더 시도
        if not row:
            print("[DEBUG] 정확 매칭 실패 → LIKE 매칭 시도")
            query2 = """
                SELECT message_id, original_code
                FROM original_code
                WHERE original_code LIKE %s
                LIMIT 1;
            """
            cur.execute(query2, (f"%{clean}%",))
            row = cur.fetchone()

        if not row:
            print("[DEBUG] original_code 를 DB에서 찾을 수 없습니다.")
            cur.close()
            conn.close()
            return None

        msg_id = row["message_id"]

        # messages 에서 frame_id 조회
        can_id = None
        if msg_id is not None:
            query_msg = """
                SELECT frame_id
                FROM messages
                WHERE id = %s
                LIMIT 1;
            """
            cur.execute(query_msg, (msg_id,))
            msg_row = cur.fetchone()
            print("[DEBUG] messages 조회 결과:", msg_row)
            if msg_row:
                can_id = msg_row["frame_id"]

        cur.close()
        conn.close()
        return can_id

    except Error as e:
        messagebox.showerror("DB 조회 에러", f"신호 정보를 조회하는 중 에러가 발생했습니다.\n\n{e}")
        return None

# ============================================
# GUI 클래스
# ============================================
class CanAnalyzerSimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CAN 통신 해석기 (Original Code 입력용)")
        self.root.geometry("800x400")

        self.build_ui()

    def build_ui(self):
        # 상단 안내 라벨
        title = tk.Label(self.root, text="Original_code 한 줄 입력 → CAN ID & BIT 표시",
                         font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # 입력 영역
        frame_input = tk.Frame(self.root, padx=10, pady=10)
        frame_input.pack(fill="x")

        lbl = tk.Label(frame_input, text="original_code 입력", font=("Arial", 11))
        lbl.pack(anchor="w")

        # original_code가 길 수 있으니 Entry 대신 Text 사용 (한 줄 입력도 가능)
        self.txt_original = tk.Text(frame_input, height=3, font=("Consolas", 10))
        self.txt_original.pack(fill="x", pady=5)

        btn = tk.Button(frame_input, text="해석", width=10,
                        command=self.on_analyze_clicked, bg="#f7eaea")
        btn.pack(anchor="e", pady=5)

        # 결과 영역
        frame_result = tk.Frame(self.root, padx=10, pady=10)
        frame_result.pack(fill="x")

        self.lbl_can_id = tk.Label(frame_result, text="CAN ID: ",
                                   bg="#f0f0f0", anchor="w",
                                   padx=10, pady=10, relief="solid", bd=1,
                                   font=("Consolas", 11))
        self.lbl_can_id.pack(fill="x", pady=5)

        self.lbl_bit = tk.Label(frame_result, text="BIT: ",
                                bg="#f0f0f0", anchor="w",
                                padx=10, pady=10, relief="solid", bd=1,
                                font=("Consolas", 11))
        self.lbl_bit.pack(fill="x", pady=5)

    def on_analyze_clicked(self):
        original = self.txt_original.get("1.0", tk.END).strip()
        if not original:
            messagebox.showwarning("알림", "original_code 한 줄을 입력하세요.")
            return

        # 1) 입력된 original_code에서 start_bit, bit_length 파싱
        start_bit, bit_length = parse_bits_from_original_code(original)
        if start_bit is None or bit_length is None:
            messagebox.showwarning("알림", "original_code에서 비트 정보를 파싱할 수 없습니다.")
            return

        # 2) original_code 기준으로 CAN ID 조회
        can_id = get_can_id_by_original_code(original)

        if can_id is None:
            self.lbl_can_id.config(text="CAN ID: (조회 실패)")
        else:
            self.lbl_can_id.config(text=f"CAN ID: {can_id}")

        # 3) 비트 마스크 계산 및 표시
        bit_bytes = calculate_bits(start_bit, bit_length)
        bit_str = " ".join(f"{b:02X}" for b in bit_bytes)
        self.lbl_bit.config(text=f"BIT: {bit_str}")

# ============================================
# 실행
# ============================================
if __name__ == "__main__":
    root = tk.Tk()
    app = CanAnalyzerSimpleApp(root)
    root.mainloop()
