## ==============================================
## ML_CV 가상환경에 설치된 패키지 버전체크
## ==============================================
## 모듈 로딩
import cv2
import numpy as np
import sklearn as sk
import pandas as pd
import matplotlib as mp


## 패키지별 버전 정보 출력
print(f'OpenCV       v.{cv2.__version__}')
print(f'Numpy        v.{np.__version__}')
print(f'Pandas       v.{pd.__version__}')
print(f'Scikit-learn v.{sk.__version__}')
print(f'Matplotlib   v.{mp.__version__}')