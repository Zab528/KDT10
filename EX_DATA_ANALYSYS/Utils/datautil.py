## ==============================================================
## DATA에 관련된 공통된 함수들 (예: 속성 출력 기능 함수...)
## ==============================================================
import numpy as np

## ==============================================================
## 함수이름 : print_info
## 함수기능 : DataFrame, Series의 속성 정보 출력
## 매개변수 : obj     - DataFrame 또는 Series 인스턴스
##           name    - DataFrame 또는 Series 이름
##           isDF    - DataFrame 여부 [기] True
## 반환결과 : 없음
## ==============================================================
def print_info(obj, name, isDF=True):
    print(f'\n[{name}]==========')
    print(f'obj.index   : {obj.index}')
    if isDF:
        print(f'obj.columns : {obj.columns}')
    print(f'obj.shape   : {obj.shape}')
    print(f'obj.ndim    : {obj.ndim}D')
    if isDF:
        print(f'obj.dtypes   :\n{obj.dtypes}')
    else:
        print(f'obj.dtype    : {obj.dtype}')


## ==============================================================
## 함수이름 : summary
## 함수기능 : DataFrame, Series의 기본 정보 및 통계값 출력
## 매개변수 : obj       - DataFrame 또는 Series 인스턴스
##           include_  - 수치 컬럼 또는 모든 컬럼 설정 [기] None
## 반환결과 : 없음
## ==============================================================
def summary(obj,include_=None):
    print(obj.head(3))
    obj.info()
    print(obj.describe(include=include_))


## ==============================================================
## 함수이름 : check_unique
## 함수기능 : 컬럼별 고유값, 고유값 개수, 타입 출력 함수
## 매개변수 : obj   - DataFrame 인스턴스
## 반환결과 : 없음
## ==============================================================
def check_unique(obj):
    ## 컬럼별 고유값 검사 => unique() / nunique()
    for col in obj.columns:
        print(f'[{col}] =====> {obj[col].nunique()}개/{obj[col].dtype}')
        print(obj[col].unique())