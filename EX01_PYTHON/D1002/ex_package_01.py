## ------------------------------------------------------------
## 모듈 사용하기
## - 패키지 : 유사한 기능/목적의 모듈들을 하나로 묶어서 관리하는 것
## - 사  용 : import 패키지명.모듈명
##           import 패키지명.모듈명 as 약칭
##           from 패키지명.모듈명 import 변수, 함수, 클래스
##           from 패키지명.모듈명 import *
## ------------------------------------------------------------
## 모듈 로딩
## ------------------------------------------------------------
import urllib.request as req           

## ------------------------------------------------------------
## 모듈의 변수, 함수, 클래스 사용 => 모듈명.변수명 / 모듈명.함수명()
## ------------------------------------------------------------
## req.urlopen(URL) : 해당 URL에 대한 정보를 HTTPResponse객체에 담아서 반환
##                    데이터에 대한 다양한 작업
data = req.urlopen("https://docs.python.org/3.11/tutorial/index.html")
print(f'data => { type(data) }')
print(f'data.url => { data.url }')
print(f'data.status => { data.status }')
print(f'data.read => { data.read() }')

## req.urlopen(URL) : 해당 URL에 대한 정보를 HTTPResponse객체에 담아서 반환
##                    데이터에 대한 다양한 작업
IMG_URL='https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcS1_hrqnqzg6eUthXW17yE-tCDHBSVUSFZK279Q6gTC-Sfv1ohJb8Kw4BpSQBpsGQsKPo7Me9LaXksDlcwiu0RY7k8kPChTh0AGse0SgLw9kQ'
req.urlretrieve(IMG_URL, "dog.jpg")