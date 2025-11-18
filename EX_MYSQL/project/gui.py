import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import math
import mysql.connector
from mysql.connector import Error

# ============================================
# original_code → 신호 이름 추출
# 예: "SG_ Pas_Spkr_Rrh_Alarm : 60|2@..." → "Pas_Spkr_Rrh_Alarm"
# ============================================
def extract_signal_name(original_code: str) -> str:
    s = original_code.strip()
    if s.startswith("SG_"):
        s = s[3:].lstrip()
    for sep in [":", " "]:
        idx = s.find(sep)
        if idx != -1:
            return s[:idx]
    return s

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

def parse_bits_from_original_code(original_code: str):
    """
    예: 'SG_ SAS_Angle : 0|16@little_endian 0.1 0.0 Deg'
    → start_bit = 0, bit_length = 16
    """
    try:
        # ':' 뒤쪽만 잘라서
        after_colon = original_code.split(":", 1)[1].strip()
        # '@' 앞까지만 사용 → '0|16'
        before_at = after_colon.split("@", 1)[0].strip()
        start_str, length_str = before_at.split("|")
        return int(start_str), int(length_str)
    except Exception:
        # 파싱 실패 시 기본값
        return None, None



# ============================================
# 신호 이름으로 CAN ID / start_bit / bit_length 조회
# ============================================
def get_signal_info(signal_name: str):
    conn = get_conn()
    if conn is None:
        return None

    try:
        cur = conn.cursor(dictionary=True)

        # 1) original_code에서 signal_name으로 한 줄 찾기
        query_oc = """
            SELECT id, message_id, signal_name, original_code
            FROM original_code
            WHERE signal_name = %s
            LIMIT 1;
        """
        cur.execute(query_oc, (signal_name,))
        oc_row = cur.fetchone()

        if not oc_row:
            # original_code 자체에 없으면 그냥 종료
            cur.close()
            conn.close()
            return None

        # 2) original_code 문자열에서 start_bit / bit_length 파싱
        start_bit, bit_length = parse_bits_from_original_code(oc_row["original_code"])

        # 3) message_id로 messages에서 frame_id 조회 (있으면)
        can_id = None
        msg_id = oc_row.get("message_id")

        if msg_id is not None:
            query_msg = """
                SELECT frame_id
                FROM messages
                WHERE id = %s
                LIMIT 1;
            """
            cur.execute(query_msg, (msg_id,))
            msg_row = cur.fetchone()
            if msg_row:
                can_id = msg_row["frame_id"]

        cur.close()
        conn.close()

        # 4) 리턴 (CAN ID 없어도 bit 정보만이라도 리턴)
        return {
            "can_id": can_id,
            "start_bit": start_bit,
            "bit_length": bit_length,
        }

    except Error as e:
        messagebox.showerror("DB 조회 에러", f"신호 정보를 조회하는 중 에러가 발생했습니다.\n\n{e}")
        return None




# ============================================
# 클래스 정의 (CarPoint)
# ============================================
class CarPoint:
    def __init__(self, id, name, x, y):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.color = "red"  # 초기 색상

    def toggle_color(self):
        self.color = "green" if self.color == "red" else "red"

# ============================================
# 메인 애플리케이션 클래스
# ============================================
class CanAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CAN 통신 해석기")
        self.root.geometry("1200x700")

        # UI 레이아웃 설정 (좌/우 분할)
        self.setup_layout()
        
        # 초기 데이터 로드 및 캔버스 설정
        self.load_image_and_points()

    def setup_layout(self):
        # --- 1. 왼쪽 패널 (컨트롤 및 결과) ---
        left_frame = tk.Frame(self.root, width=400, padx=20, pady=20)
        left_frame.pack(side="left", fill="y")
        left_frame.pack_propagate(False)  # 크기 고정

        tk.Label(left_frame, text="~ CAN 통신 해석 ~", font=("Arial", 20, "bold")).pack(pady=(0, 30))

        # 검색 영역
        search_frame = tk.Frame(left_frame)
        search_frame.pack(fill="x", pady=10)

        tk.Label(search_frame, text="CAN 통신값 검색").pack(anchor="w")
        
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12))
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

        btn_analyze = tk.Button(search_frame, text="해석", command=self.analyze_can, bg="#f7eaea", width=8)
        btn_analyze.pack(side="left", padx=2)

        btn_log = tk.Button(search_frame, text="로그", command=lambda: print("로그 버튼 클릭됨"), bg="#f7eaea", width=8)
        btn_log.pack(side="left", padx=2)

        # 결과 표시 영역
        self.result_frame = tk.Frame(left_frame, pady=20)
        self.result_frame.pack(fill="x")

        self.lbl_can_id = tk.Label(self.result_frame, text="", bg="#f0f0f0",
                                   anchor="w", padx=10, pady=10, relief="solid", bd=1)
        self.lbl_bit = tk.Label(self.result_frame, text="", bg="#f0f0f0",
                                anchor="w", padx=10, pady=10, relief="solid", bd=1)

        tk.Label(left_frame, text="").pack()  # 여백

        self.box1 = tk.Label(left_frame, text="DB에서 가져온 결과 1", bg="#f7eaea",
                             height=10, relief="flat", anchor="nw", padx=10, pady=10, font=("Arial", 11))
        self.box1.pack(fill="x", pady=10)

        self.box2 = tk.Label(left_frame, text="DB에서 가져온 결과 2", bg="#e0e0e0",
                             height=10, relief="flat", anchor="nw", padx=10, pady=10, font=("Arial", 11))
        self.box2.pack(fill="x", pady=10)

        # --- 2. 오른쪽 패널 (자동차 이미지 캔버스) ---
        self.right_frame = tk.Frame(self.root, bg="white")
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.canvas = tk.Canvas(self.right_frame, bg="white", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def load_image_and_points(self):
        try:
            self.orig_image = Image.open("car.png")
            self.tk_image = ImageTk.PhotoImage(self.orig_image)
            
            self.canvas_width = 800
            self.img_w, self.img_h = self.orig_image.size
            
            self.canvas.create_image(self.canvas_width//2, self.img_h//2 + 20,
                                     image=self.tk_image, anchor="center")
            
            x = self.canvas_width // 2 + 15
            
            self.points = [
                CarPoint("FL_Corner", "Front_Left_Sensor", x - 90, 45),
                CarPoint("FR_Corner", "Front_Right_Sensor", x + 90, 45),
                CarPoint("Side_L", "Side_Mirror_L", x - 130, 220),
                CarPoint("Side_R", "Side_Mirror_R", x + 130, 220),
                CarPoint("Seat_FL", "Driver_Seat", x - 45, 290),
                CarPoint("Seat_FR", "Passenger_Seat", x + 45, 290),
                CarPoint("Door_FL", "Door_Front_L", x - 120, 310),
                CarPoint("Door_FR", "Door_Front_R", x + 120, 310),
                CarPoint("Seat_RL", "Rear_Seat_L", x - 45, 400),
                CarPoint("Seat_RR", "Rear_Seat_R", x + 45, 400),
                CarPoint("Door_RL", "Door_Rear_L", x - 120, 430),
                CarPoint("Door_RR", "Door_Rear_R", x + 120, 430),
                CarPoint("RL_Corner", "Rear_Left_Sensor", x - 100, 570),
                CarPoint("RR_Corner", "Rear_Right_Sensor", x + 100, 570),
            ]
            
            self.draw_points()

        except FileNotFoundError:
            messagebox.showerror("에러", "car.png 파일을 찾을 수 없습니다.\n같은 폴더에 이미지를 넣어주세요.")

    def analyze_can(self):
        original = self.search_entry.get().strip()
        if not original:
            messagebox.showwarning("알림", "CAN 통신 한 줄을 입력하세요.")
            return

        # SG_ ... 에서 SAS_Angle만 쏙 뽑기
        signal_name = extract_signal_name(original)
        info = get_signal_info(signal_name)
        print("여기띠: ",signal_name)

        if info:
            can_id = info.get("can_id")
            start_bit = info.get("start_bit")
            bit_length = info.get("bit_length")

            self.lbl_can_id.config(text=f"CAN ID: {can_id}")
            self.lbl_can_id.pack(fill="x", pady=5)

            self.lbl_bit.config(text=f"BIT: {start_bit} | {bit_length}")
            self.lbl_bit.pack(fill="x", pady=5)

            self.box1.config(text=f"신호 이름: {signal_name}\nCAN ID: {can_id}")
            self.box2.config(text=f"start_bit: {start_bit}\nbit_length: {bit_length}")
        else:
            self.lbl_can_id.pack_forget()
            self.lbl_bit.pack_forget()
            messagebox.showwarning("알림", f"'{signal_name}' 에 해당하는 신호를 찾을 수 없습니다.")


    def draw_points(self):
        self.canvas.delete("dots")
        r = 10
        for p in self.points:
            self.canvas.create_oval(
                p.x - r, p.y - r, p.x + r, p.y + r,
                fill=p.color, outline="black", tags="dots"
            )

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        clicked = False
        
        for p in self.points:
            distance = math.hypot(p.x - x, p.y - y)
            if distance < 15:
                p.toggle_color()
                clicked = True
        
        if clicked:
            self.draw_points()

# ============================================
# 실행
# ============================================
if __name__ == "__main__":
    root = tk.Tk()
    app = CanAnalyzerApp(root)
    root.mainloop()
