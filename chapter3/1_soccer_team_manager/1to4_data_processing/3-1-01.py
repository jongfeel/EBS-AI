# 파일에 저장한 데이터를 불러와 출력하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')        # fifa2019.csv 파일의 데이터 불러오기

print(fifa2019.shape)                         # 출력하기

