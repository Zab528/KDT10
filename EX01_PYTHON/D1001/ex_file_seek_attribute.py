## -------------------------------------------------------------------------------
## 파일 입출력
## - 파일 위치 관련 메서드
##             * seek( offset ) : 파일 포인터의 위치 설정
##             * tell()         : 현재 파일 포인터의 위치 알려줌
## - 파일 속성 관련 변수
##            * closed  : 닫혔는지 여부 True/False
##            * mode    : 현재 파일의 모드
##            * name    : 현재 파일 이름
## -------------------------------------------------------------------------------
## 파일 설정
F_NAME = './data.txt'

with open(F_NAME, mode='r', encoding='utf-8') as F:
    while True:
        line = F.readline()
        print(line)
        if not len(line) : break
        print(f'현재 파일포인트 위치 : {F.tell()}')

    ## 한번 더 읽기
    print('--- 한 번 더 읽기 ---')
    F.seek(0)                   ## 파일 포인터를 처음으로 이동
    while True:
        line = F.readline()
        print(line)
        if not len(line) : break
        print(f'현재 파일포인트 위치 : {F.tell()}')

## => 현재 파일의 속성 및 상태
print("END")
print(f'F.closed : {F.closed}')
print(f'F.mode   : {F.mode}')
print(f'F.name   : {F.name}')