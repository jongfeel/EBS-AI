# 궁금한 선수의 데이터 검색하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

# --------------------------------------------

sub1 = fifa2019.loc[14]      # fifa2019의 인덱스 레이블 14인 행값을 sub1에 저장
print(sub1)

