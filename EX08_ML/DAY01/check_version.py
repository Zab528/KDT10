## --------------------------------------------------
### ML 가상환경 설치 패키지 버전 확인
## --------------------------------------------------
import pandas as pd
import sklearn as sk
import numpy as np
import matplotlib as ma
import seaborn as sns

## 설치 패키지별 버전 출력
print(f'pandas      v.{pd.__version__}')
print(f'scikitlearn v.{sk.__version__}')
print(f'numpy       v.{np.__version__}')
print(f'matplotlib  v.{ma.__version__}')
print(f'seaborn     v.{sns.__version__}')