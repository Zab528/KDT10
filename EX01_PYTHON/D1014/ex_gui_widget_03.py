## ==========================================================
## Python GUI Programming - TKinter
##
## ** Label Widget : 텍스트, 이미지 출력 UI요소
## ==========================================================
## 모듈 로딩
## ==========================================================
from tkinter import *

import os                        ## 이미지 경로 관련 모듈
from PIL import Image, ImageTk   ## TK 미지원 이미지 처리 위한 모듈

## ----------------------------------------------------------
##- 사용자 정의 함수
## ----------------------------------------------------------
##- 함수기능 : 이미지 데이터에서 Tkinter용 이미지 추출 후 반환
##- 함수이름 : get_img
##- 매개변수 : imgpath       - 이미지용 포함 경로
##- 반환결과 : Tkinter용 이미지 데이터
## ----------------------------------------------------------
def get_img(filepath):
    ## => 지원&미지원 이미지 처리
    _ , ext = os.path.splitext(filepath)
    if ext in ['.png', '.bmp', '.gif', '.ppm', '.pgm']:
        return PhotoImage(file=filepath)
    else:
        #- 순수 이미지 데이터 추출
        img = Image.open(filepath)
        #- 이미지 데이터 전달
        return ImageTk.PhotoImage(image=img)
    


##- 윈도우 창 인스턴스 생성
mainWind=Tk()

##- 윈도우 창에 설정
## 창 제목
mainWind.title("MY APP")
# 창 크기와 위치 : "너비x높이+x좌표+y좌표"
mainWind.geometry("1000x500+400+200")  ## "너비x높이+x좌표+y좌표"
## 창 크기 조절 : (WIDTH, HEIGHT)
mainWind.resizable(False, True)

## ----------------------------------------------------------
##- 윈도우에 배치될 UI 요소들 - Image Label 요소
##- 지  원 이미지 확장자 : .png, .bmp, .gif, .ppm, .pgm
##- 미지원 이미지 경  우 : 로우 데이터 추출 필요 => conda install pillow
## ----------------------------------------------------------
## 인스턴스 생성
## => 지원 이미지 : png, bmp, gif, ppm, prn
IMG_FILE1 = '../Image/bear.png'
IMG_FILE2 = '../Image/fire.jpg'
IMG_FILE3 = '../Image/moon.jpg'

img1 = get_img(IMG_FILE1)
img2 = get_img(IMG_FILE2)
img3 = get_img(IMG_FILE3)
##- 이미지 라벨 인스턴스 생성
imgLB1 = Label(mainWind, image=img1)
imgLB2 = Label(mainWind, image=img2)
imgLB3 = Label(mainWind, image=img3)

## UI 인스턴스 윈도우에 배치
imgLB1.pack(side='left')
imgLB2.pack()
imgLB3.pack(side='right')


## ----------------------------------------------------------
##- 윈도우에서 발생하는 이벤트 메시지 수신
## ----------------------------------------------------------
##- 종료 전까지 동작
mainWind.mainloop()