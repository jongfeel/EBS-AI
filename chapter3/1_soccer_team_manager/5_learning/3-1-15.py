# K-평균 군집화 알고리즘 적용하기 - 각 군집의 중심을 새롭게 계산하기

import pandas as pd


fifa2019 = pd.read_csv('fifa2019.csv')
df = pd.DataFrame.copy(fifa2019.sort_values(by = 'Overall', ascending = False ).head(200))
test_features=['Name','Stamina','Dribbling','ShortPassing','Penalties']
test_df= pd.DataFrame(df , columns = test_features)


# 학습 데이터 준비하기
import numpy as np 
XY = np.array(test_df)
X = XY[:,1:3]


# 표본공간에 k개의 중심을 무작위로 생성하기
k = 3                               #분류하려는 군집의 개수가 3개이므로 k=3
C_x = np.random.choice(X[:,0],k,replace=False)
C_y = np.random.choice(X[:,1],k,replace=False)
C = np.array(list(zip(C_x, C_y)))


# 거리를 측정하는 함수 만들기 
# 유클리디안 거리 계산 함수 만들기
def Distance(A, B):
    return np.sqrt(np.sum(np.power((A-B),2)))

# 각 군집의 중심을 새롭게 계산하기 

C_old = np.zeros(C.shape)           # 중심의 좌표를 업데이트하기 위해 동일한 크기의 행렬을 선언 
clusters = np.zeros(len(X))         # 모든 데이터의 클러스터 라벨을 저장하기 위해 행렬을 선언, 초깃값은 0으로 할당
flag = Distance(C, C_old)           # 반복문의 종료 기준이 될 변수 선언, 중심 C의 좌표가 더이상 변화가 없을 때까지 반복하는 기준이 됨.

# ---------------------------------------------------------------------------------

# 클러스터 할당이 변경되지 않을 때까지 반복하기
from copy import deepcopy

distances = []
while flag !=0:                     #SSE
    for i in range(len(X)):
      for j in range(3):
        temp = Distance(X[i], C[j])
        distances.append(temp)
      cluster = np.argmin(distances)
      clusters[i] = cluster
      distances = []
    C_old = deepcopy(C)
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        C[i] = np.mean(points)
    flag = Distance(C, C_old)
    
# 군집화 결과 시각화하기
import matplotlib.pyplot as plt

# 1번 군집
plt.scatter(X[clusters == 0,0], X[clusters == 0,1], s=50, c='red', marker='o', edgecolor='black', label='A')
            
# 2번군집
plt.scatter(X[clusters == 1,0], X[clusters == 1,1], s=50, c='yellow', marker='x', edgecolor='black', label='B')

# 3번 군집
plt.scatter(X[clusters == 2,0], X[clusters == 2,1], s=50, c='blue', marker='^', edgecolor='black', label='C')

# 군집의 중심 좌표들
plt.scatter(C[:, 0], C[:, 1], s=250, marker='*', c='black', edgecolor='black', label='Centroids')
plt.legend()
plt.grid()
plt.show()
