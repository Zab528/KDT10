## ==========================================================
## Python GUI Programming - TKinter
## ==========================================================
## 모듈 로딩
## ==========================================================
from tkinter import *

##- 윈도우 창 생성
mainWind=Tk()

##- 윈도우 창에 설정
## 창 제목
mainWind.title("MY APP")
# 창 크기와 위치 : "너비x높이+x좌표+y좌표"
mainWind.geometry("1000x200+500+700")  ## "너비x높이+x좌표+y좌표"
## 창 크기 조절 : (WIDTH, HEIGHT)
mainWind.resizable(False, True)

##- 윈도우에서 발생하는 이벤트 메시지 수신
##- 종료 전까지 동작
mainWind.mainloop()