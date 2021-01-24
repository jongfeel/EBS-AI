# 선수들이 선호하는 발의 종류를 원 그래프로 나타내기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

import matplotlib.pyplot as plt         # 그래프를 출력하기 위한 모듈

# ---------------------------------------------------------------------

fifa2019['Preferred Foot'].value_counts().plot(kind='pie', autopct='%1.f%%', legend=True)
#plt.legend()                            # 범례 표시하기
plt.show()                              # 그래프 출력하기
