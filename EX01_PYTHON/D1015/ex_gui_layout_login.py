## ====================================================================
##              Python GUI Programming - TKinter 
## ====================================================================
## LogIn 화면 구성
## - 사용 Widget
##   * Label   -  타이틀/아이디/비밀번호  3개
##   * Entry   -  아이디/비밀번호        2개
##   * Button  -  확인/취소             2개
## - 배치 Layout
##   * 표 형식의 Grid
## ====================================================================

## --------------------------------------------------------------------
## 모듈 로딩 
## --------------------------------------------------------------------
import tkinter

## --------------------------------------------------------------------
##- 윈도우 관련 
## --------------------------------------------------------------------
##- 윈도우 창 인스턴스 생성
window=tkinter.Tk()
window.title("LogIn")
window.geometry("400x200+500+200")
window.resizable(False,False)

## --------------------------------------------------------------------
##- 윈도우에 배치될 UI요소들 - Button 요소
## --------------------------------------------------------------------
## - Button 인스턴스 생성
msgLB1 = tkinter.Label(text="LOGIN")
msgLB2 = tkinter.Label(text="ID")
msgLB3 = tkinter.Label(text="PW")

inputFD1 = tkinter.Entry(window)
inputFD2 = tkinter.Entry(window)

okBTN = tkinter.Button(window,
                       text="OK",
                       padx=30)
caBTN = tkinter.Button(window,
                       text="CANCEL",
                       padx=15)



##-  배치
msgLB1.grid(row=0, column=3)
msgLB2.grid(row=1, column=2)
msgLB3.grid(row=2, column=2)

inputFD1.grid(row=1, column=3)
inputFD2.grid(row=2, column=3)

okBTN.grid(row=6, column=3)
caBTN.grid(row=6, column=4)

## --------------------------------------------------------------------
##- 윈도우에서 발생하는 사용자 이벤트 수신
## --------------------------------------------------------------------
##- 종료 전까지 동작
window.mainloop()