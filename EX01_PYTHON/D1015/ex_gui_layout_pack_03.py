## ====================================================================
##              Python GUI Programming - TKinter 
## ====================================================================
## Container Layout : Pack
##   * 왼쪽/오른쪽/위/아래/가운데로 지정된 위치에 UI요소 배치
##   * grid()와 같이 사용될 수 없음. place()와 같이 사용할 수 있음
##   * 배치되는 우선 순위
##      - 가장 처음 선언한 pack부터 배치
##      - pack의 매개변수로 인하여 위젯의 크기가 변경될 수 있음
##   * 사용법
##     위젯이름.pack(매개변수1, 매개변수2, 매개변수3, ...)
##   * 주요 매개변수
##     side   : 해당 구역으로 위젯을 이동시킴
##              'left', 'right', 'top', 'bottom'
##     anchor : 현재 배치된 구역 안에서 특정 위치로 이동시킴.
##        n (north): 위젯을 셀의 상단에 붙임
##        e (east) : 위젯을 셀의 오른쪽에 붙임
##        s (south): 위젯을 셀의 하단에 붙임
##        w (west) : 위젯을 셀의 왼쪽에 붙임 
##        nw (north-west): 위젯을 셀의 왼쪽 상단에 붙임
##        ne (north-east): 위젯을 셀의 오른쪽 상단에 붙임
##        sw (south-west): 위젯을 셀의 왼쪽 하단에 붙임
##        se (south-east): 위젯을 셀의 오른쪽 하단에 붙임
##     fill   : 할당된 공간에 맞게 크기가 변경됨
##     expand : 할당되지 않은 미사용 공간 모두 현재 위젯의 할당된 공간으로 변경
## ====================================================================

## --------------------------------------------------------------------
## 모듈 로딩 
## --------------------------------------------------------------------
import tkinter

## --------------------------------------------------------------------
##- 윈도우 관련 
## --------------------------------------------------------------------
##- 윈도우 창 인스턴스 생성 및 설정
window=tkinter.Tk()
window.title("LAYOUT_PACK")
window.geometry("640x400+500+200")
window.resizable(False,False)

## --------------------------------------------------------------------
##- 윈도우에 배치될 UI요소들 - Button 요소
## --------------------------------------------------------------------
##- 버튼 인스턴스 생성
b1 = tkinter.Button(window, text="left-1")
b1_1=tkinter.Button(window, text="left-2")

b2 = tkinter.Button(window, text="left-3")
b2_1=tkinter.Button(window, text="left-4")

b3 = tkinter.Button(window, text="left-5")
b3_1=tkinter.Button(window, text="left-6")

b4 = tkinter.Button(window, text="left-7")
b4_1=tkinter.Button(window, text="left-8")

#b5 = tkinter.Button(window, text="center", bg="red")


##- 버튼 인스턴스를 화면에 pack 방식으로 자동 배치
b1.pack(side="left")                     ##- [기본] 버튼위에 text 보여질 만큼 W, H 크기로 버튼 배치
b1_1.pack(side="left", fill="x")         ##- side='top'인 경우 가로(x축)공간만 확장 가능함

b2.pack(side="left")
b2_1.pack(side="left", anchor="e")

b3.pack(side="left")
b3_1.pack(side="left", fill="y")

b4.pack(side="left")
b4_1.pack(side="left", anchor="s")


#b5.pack(expand=True, fill="both")
#b5.pack(expand=True)                   

## --------------------------------------------------------------------
##- 윈도우에서 발생하는 사용자 이벤트 수신
## --------------------------------------------------------------------
##- 종료 전까지 동작
window.mainloop()