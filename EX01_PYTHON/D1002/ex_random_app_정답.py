## -----------------------------------------------------
##              내장 모듈 random 활용
## - random -> 난수 생성하거나 무작위 선택 할 때 사용
## -----------------------------------------------------
## [실습1] 로또 프로그램을 구현하세요.
##        - 숫자 범위 : 1 ~ 45
##        - 추출 숫자 : 6개 중복 X
##        - 조    건 : randint 사용
## -----------------------------------------------------
## [방법1]
from random import randint

lotto=[]
while True:
    if len(lotto) == 6: break

    num = randint(1,45)
    if num not in lotto:
        lotto.append(num)

print(f'이번 주 로또 번호 : {lotto}')


## [방법2] ==> random 중복 불허를 위해 처음부터 리스트가 아닌 set 사용하자
## set 타입 : 중복 불허!
lotto=set()
while True:
    if len(lotto) == 6: break
    lotto.add(randint(1,45))

print(f'이번 주 로또 번호 : {lotto}')

## [방법3] ==> sample로 뽑아서 처음부터 중복 방지
from random import sample

print(f'이번 주 로또 번호 : {sample(range(1,46), 6)}')