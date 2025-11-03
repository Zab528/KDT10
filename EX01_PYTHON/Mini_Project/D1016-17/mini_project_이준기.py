## ------------------------------------------------------------------------
##                            Mini_Project
## 주제 : OTT 결제 계산기 만들기
## 목적 : OTT 결제 가격, 마감일 등에 대한 계산과 암기를 편하게 하기 위해
## 기능 : GUI를 통해 OTT명, 개월 수, 시작일을 입력하면
##       그것에 맞는 가격과 마감일이 출력란에 출력
##       => 입력은 버튼을 통해서 원하는 버튼을 클릭하면 자동으로 입력란에 입력
## ------------------------------------------------------------------------
##                          (프로토타입 모양)
##      ----------------------------------------------------------------
##      |            OTT Calculator                 GO!                |
##      |                                                              |
##      |         OTT 명 :                                              |
##      |         개월 수 :                                             |
##      |         가  격  :                                             |
##      |         시작일  :                                             |
##      |         마감일  :                                             |
##      |                                                              |
##      |         유튜브         티빙              넷플릭스        디즈니  |
##      |                                                              |
##      |         1개월         3개월              6개월          12개월  |
##      |                                                              |
##      |                                                              |
##      ----------------------------------------------------------------

## ------------------------------------------------------------------------

## --------------------------------------------------------------------
## 모듈 로딩 
## --------------------------------------------------------------------
import tkinter
from datetime import date, timedelta
from PIL import Image, ImageTk

## --------------------------------------------------------------------
##- 윈도우 관련 
## --------------------------------------------------------------------
##- 윈도우 창 인스턴스 생성 및 설정
window=tkinter.Tk()
window.title("★★ OTT Calculator ★★")
window.geometry("320x420")

##- 전역변수
ROWS = 8
COLS = 4

##- OTT별 월 결제 금액
PRICE_TABLE = {
    "유튜브": 14900,
    "티빙": 5500,
    "넷플릭스": 7000,
    "디즈니": 9900,
}

## ------------------------------------------------------
## 함수기능 : 모든 행/열을 동일 비율로 설정
## 함수이름 : make_equal_grid
## 매개변수 : parent
##           rows
##           cols
## 결과반환 : 없음
## ------------------------------------------------------
def make_equal_grid(parent, rows, cols):
    #모든 행/열을 동일 비율로
    for r in range(rows):
        parent.grid_rowconfigure(r, weight=1, uniform='row')
    for c in range(cols):
        parent.grid_columnconfigure(c, weigh=1, uniform='col')

## ------------------------------------------------------
## 함수기능 : Grid를 함수로 호출
## 함수이름 : make_grid
## 매개변수 : w, r, c, rs, cs, padx, pady, sticky
## 결과반환 : 없음
## ------------------------------------------------------
def make_grid(w, r, c, rs=1, cs=1, padx=4, pady=4, sticky="nsew"):
    w.grid(row=r, column=c, rowspan=rs, columnspan=cs, padx=padx, pady=pady, sticky=sticky)

## ------------------------------------------------------
## 함수기능 : entry안에 입력을 세팅
## 함수이름 : set_entry
## 매개변수 : entry, text
## 결과반환 : 없음
## ------------------------------------------------------
def set_entry(entry, text):
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, text)

## ------------------------------------------------------
## 함수기능 : 시작일 입력을 구분해준다
## 함수이름 : parse_date
## 매개변수 : s
## 결과반환 : date
## ------------------------------------------------------
def parse_date(s):
    try:
        y, m, d = map(int, s.split('-'))
        if y < 100:
            y += 2000
        return date(y, m, d)
    except:
        return None

## ------------------------------------------------------
## 함수기능 : 시작일에서 30일을 더해주는 함수
## 함수이름 : add_30days
## 매개변수 : start_str, months
## 결과반환 : 없음
## ------------------------------------------------------
def add_30days(start_str, months):  
    start = parse_date(start_str)
    end = start + timedelta(days=30 * months)      
    end_inclusive = end - timedelta(days=1)
    return end_inclusive.strftime("%y-%m-%d")

## ------------------------------------------------------
## 함수기능 : OTT명에 OTT 입력
## 함수이름 : OTT_SET
## 매개변수 : name
## 결과반환 : 없음
## ------------------------------------------------------
def OTT_SET(name):
    OTTENT.delete(0, tkinter.END)
    OTTENT.insert(tkinter.END, name)

## ------------------------------------------------------
## 함수기능 : 개월 수에 개월 입력
## 함수이름 : MON_SET
## 매개변수 : m
## 결과반환 : 없음
## ------------------------------------------------------
def MON_SET(m):
    MonthENT.delete(0, tkinter.END)
    MonthENT.insert(tkinter.END, m)

## ------------------------------------------------------
## 함수기능 : 계산 버튼을 통해 가격과 마감일 계산
## 함수이름 : CALC
## 매개변수 : -
## 결과반환 : 없음
## ------------------------------------------------------
def CALC():
    name = OTTENT.get().strip()
    months_text = MonthENT.get().strip()
    start_text  = StartENT.get().strip()

    # --- 가격 계산  ---
    if name in PRICE_TABLE and months_text.isdigit():
        months = int(months_text)
        unit   = PRICE_TABLE[name]
        total  = unit * months
        set_entry(PriceENT, f'{total:,}')
    else:
        set_entry(PriceENT, "ERR")

    # --- 마감일 계산: 30일 * 개월수 ---
    dt = parse_date(start_text)
    if dt and months_text.isdigit():
        months = int(months_text)
        end = dt + timedelta(days=30 * months) 
        set_entry(EndENT, end.strftime("%y-%m-%d"))
    else:
        set_entry(EndENT, "ERR")

## --------------------------------------------------------------------
##- 윈도우에 배치될 UI요소들 - 인스턴스 생성
## --------------------------------------------------------------------
# 함수 호출
make_equal_grid(window, ROWS, COLS)
##- 0번행 타이틀, 계산 : Label + Button
titleLB = tkinter.Label(window, text="OTT Calculator", bd=1, relief='solid')
CALCBTN  = tkinter.Button(window, text="GO!", command=CALC)

##- 1번행 OTT명 입력 : Label + Entry
OTTLB  = tkinter.Label(window, text="OTT명 : ", bd=1, relief="solid")
OTTENT = tkinter.Entry(window)

##- 2번행 개월 수 입력 : Label + Entry
MonthLB = tkinter.Label(window, text="개월 수 :", bd=1, relief="solid")
MonthENT = tkinter.Entry(window)

##- 3번행 가격 출력 : Label + Entry
PriceLB = tkinter.Label(window, text="가  격 :", bd=1, relief="solid")
PriceENT = tkinter.Entry(window)

##- 4번행 시작일 입력 : Label + Entry
StartLB = tkinter.Label(window, text="시작일 :", bd=1, relief="solid")
StartENT = tkinter.Entry(window)

##- 5번행 마감일 출력 : Label + Entry
EndLB = tkinter.Label(window, text="마감일 :", bd=1, relief="solid")
EndENT = tkinter.Entry(window)

##- 6번행 OTT 선택 : Button
YBTN = tkinter.Button(window, text="유튜브")
NBTN = tkinter.Button(window, text="넷플릭스")
TBTN = tkinter.Button(window, text="티 빙")
DBTN = tkinter.Button(window, text="디즈니")


##- 7번행 결제 개월 수 선택 : Button
OneBTN = tkinter.Button(window, text="1개월")
ThrBTN = tkinter.Button(window, text="3개월")
SixBTN = tkinter.Button(window, text="6개월")
TweBTN = tkinter.Button(window, text="12개월")

## --------------------------------------------------------------------
##- 윈도우에 배치될 UI요소들 - 인스턴스 배치
## --------------------------------------------------------------------
placements = [
    (titleLB, 0, 0, 1, 3),
    (CALCBTN, 0, 3, 1, 1),

    (OTTLB,   1, 0, 1, 1),
    (OTTENT,  1, 1, 1, 3),

    (MonthLB, 2, 0, 1, 1),
    (MonthENT,2, 1, 1, 3),

    (PriceLB, 3, 0, 1, 1),
    (PriceENT,3, 1, 1, 3),

    (StartLB, 4, 0, 1, 1),
    (StartENT,4, 1, 1, 3),

    (EndLB,   5, 0, 1, 1),
    (EndENT,  5, 1, 1, 3),

    (YBTN,    6, 0, 1, 1),
    (TBTN,    6, 1, 1, 1),
    (NBTN,    6, 2, 1, 1),
    (DBTN,    6, 3, 1, 1),

    (OneBTN,  7, 0, 1, 1),
    (ThrBTN,  7, 1, 1, 1),
    (SixBTN,  7, 2, 1, 1),
    (TweBTN,  7, 3, 1, 1),
]

##- 반복문 사용해서 grid 배치
for wdg, r, c, rs, cs in placements:
    make_grid(wdg, r, c, rs, cs)

## --------------------------------------------------------------------
##- 아이콘 이미지 적용 
##  youtube.png, tving.png, netflix.png, disnep.png
## --------------------------------------------------------------------
# 공통 크기
ICON_SIZE = (40, 30)

img_y = ImageTk.PhotoImage(Image.open("youtube.png").resize(ICON_SIZE))
img_t = ImageTk.PhotoImage(Image.open("tving.png").resize(ICON_SIZE))
img_n = ImageTk.PhotoImage(Image.open("netflix.png").resize(ICON_SIZE))
img_d = ImageTk.PhotoImage(Image.open("disnep.png").resize(ICON_SIZE)) 

YBTN.config(image=img_y, text="")
TBTN.config(image=img_t, text="")
NBTN.config(image=img_n, text="")
DBTN.config(image=img_d, text="")


## --------------------------------------------------------------------
##- UI요소들 함수 사용해서 입출력 만들기
## --------------------------------------------------------------------
YBTN.config(command=lambda: OTT_SET("유튜브"))
TBTN.config(command=lambda: OTT_SET("티빙"))
NBTN.config(command=lambda: OTT_SET("넷플릭스"))
DBTN.config(command=lambda: OTT_SET("디즈니"))

OneBTN.config(command=lambda: MON_SET(1))
ThrBTN.config(command=lambda: MON_SET(3))
SixBTN.config(command=lambda: MON_SET(6))
TweBTN.config(command=lambda: MON_SET(12))



## --------------------------------------------------------------------
##- 윈도우에서 발생하는 사용자 이벤트 수신
## --------------------------------------------------------------------
##- 종료 전까지 동작
window.mainloop()






