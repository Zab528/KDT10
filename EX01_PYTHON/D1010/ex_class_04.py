## -----------------------------------------------------------
## 객체지향언어(OOP) 특성 - 정보은닉/캡슐화
## 
## - 파이썬은 모든 속성/메서드를 공개 원칙
## - 비공개 속성 설정 방법 : _ _속성명
## -----------------------------------------------------------

## -----------------------------------------------------------
## 클래스 정의 : 한국사람 데이터 타입 정의
## 클래스 이름 : KoreanPeople
## 속      성 : 나이, 이름, 성별, 주민번호, 국적
##             인스턴스 속성       => 나이, 이름, 성별, _ _주민번호
##             클래스   속성       => 국적
## 메  서  드 : 정보 출력하기       => 인스턴스 메서드
##             비공개 나이계산 기능 => _ _인스턴스 메서드
## -----------------------------------------------------------
class KoreanPeople:
    ## 클래스 속성/변수
    NATIONALITY = 'KO'

    ## 인스턴스 생성 및 속성 초기화 메서드
    def __init__(self, name_, age_, gender_, jumin_):
        self.name   = name_
        self.age    = age_
        self.gender = gender_
        self.__jumin  = jumin_     ## 외부 접근 불가용 : 비공개

    ## 인스턴스 메서드 => 개인정보 출력
    def print_info(self):
        print('*'*20)
        print(f'이   름 : {self.name}')
        print(f'성   별 : {self.gender}')
        print(f'주민번호 : {self.__jumin}개')
        print('*'*20)

    def _print_info(self):
        print('*'*20)
        print(f'이   름 : {self.name}')
        print(f'성   별 : {self.gender}')
        print(f'주민번호 : {self.__jumin}개')
        print('*'*20)
        
    ## 인스턴스 메서드 => 비공개, 나이계산
    def __calc_age(self, year):
        self.age = year - self.age

## -----------------------------------------------------------
## 속성과 메서드 활용
## -----------------------------------------------------------
## 객체/인스턴스 생성
hong  = KoreanPeople("홍길동", 20, '남자', '051050-3000000')

## 정보 출력
hong.print_info()

## 나이 변경
hong.age = 21
print(hong.age)

## 비공개 속성 주민번호 변경 => 새로운 속성으로 추가
##hong.__jumin = "1111"

## 비공개 속성 주민번호 읽기 => Error발생
#print(hong.__jumin)
#hong.__jumin = hong.__jumin + "ㅃㅃㅃㅃ"

## 비공개 메서드 사용 => Error 발생. 클래스 밖에서 사용 불가
#hong.__calc_age(2026)


print(hong.__dict__)