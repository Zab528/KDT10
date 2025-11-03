## ----------------------------------------------
## [실습]
## ----------------------------------------------
## 프로그램 : File_Explorer
## 주요기능 : Windows의 탐색기 기능
##   - 특정 폴더 아래     :  파일, 폴더 목록 출력
##   - 특정 폴더 선택     :  파일, 폴더 목록 출력 
##         파일 선택     :  크기, 생성일자 
##   - 상위 폴더 이동     :  상위 폴더의 목록 출력
## 실행화면 : 바탕화면의 목록들 
## ----------------------------------------------

import os
path = r'C:\Users\KDT\Desktop'
os.chdir(path)                 # 현재 작업 디렉토리를 바탕화면으로 변경..
files = os.listdir(path)

while True:
    print("-----현재 작업 디렉토리----- :", os.getcwd())
    files = os.listdir(os.getcwd())
    i=1
    for n in files:
        print(f'{i}. {n}')
        i += 1

    sel = input('확인하고 싶은 폴더의 이름을 입력하세요 (상위 : .. , 종료 : X) : ').strip()

    if sel == 'X':
        print('탐색 종료')
        break
    elif sel == '..':
        print("현재:", os.getcwd())
        before = os.getcwd()
        os.chdir("..")
        print("이동 후:", os.getcwd())
        if before == os.getcwd():
            print('***더 이상 이동할 수 없습니다!***')
    elif sel in files:
        full_path = os.path.join(os.getcwd(), sel)  # 현재 경로 + 선택한 이름
        print(f"\n[파일 정보]")
        print(f"디렉토리명           : {os.path.dirname(full_path)}")
        print(f"파일명               : {os.path.basename(full_path)}")
        print(f"디렉토리 + 파일 분리 : {os.path.split(full_path)}")
        print(f"확장자 분리          : {os.path.splitext(full_path)}")
        print(f"경로 존재 여부       : {os.path.exists(full_path)}")
    else:
        print('잘못된 폴더 이름입니다.')
    print()
    
