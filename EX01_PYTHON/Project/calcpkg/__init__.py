## [2] 다른 파일에 import 될 때 간략화
##     . -> 현재 위치
#from . import operation
#from . import geometry

## [3] 패키지 내 모듈들의 모든 것을 import
##     . -> 현재 위치
# from .operation import *
# from .geometry  import *

## [4] 패키지 내 모듈들의 일부만 공개하도록 설정
##     _ _all_ _ -> 매직변수코드에 설정
__all__ = ['add', 'mul', 'triangle_area']
from .operation import *
from .geometry  import *

print('__init__.py')
