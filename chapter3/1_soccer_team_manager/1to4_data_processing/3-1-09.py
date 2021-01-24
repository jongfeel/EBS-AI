# 선수들이 선호하는 발의 종류 데이터를 막대그래프로 나타내기

import pandas as pd                      # 그래프를 출력하기 위한 모듈  

fifa2019 = pd.read_csv('fifa2019.csv')

# --------------------------------------------------------------------

import matplotlib.pyplot as plt          # 그래프를 출력하기 위한 모듈

fifa2019['Preferred Foot'].value_counts().plot(kind='bar')
plt.legend()                             # 범례 표시하기
plt.show()                               # 그래프 출력하기
