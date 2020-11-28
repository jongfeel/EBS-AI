# 행렬의 성분값을 바꾸어 다른 색으로 표현하기

# 외부 모듈
import turtle                                # 그래픽 처리를 위한 모듈
import numpy as np                           # 벡터, 행렬 데이터를 쉽게 처리하기 위한 모듈


# 데이터
myImg = np.array([[0, 0, 0, 0, 0, 0, 0, 0],   #도형을 나타내는 이미지 데이터 행렬
                  [0, 1, 1, 1, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 0, 0, 0],
                  [1, 1, 1, 1, 1, 0, 0, 0],
                  [0, 1, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]])

pixelSize = 10                                 #pixel 사이즈의 반지름

# (x,y) 위치에 pSize 크기의 픽셀을 pCol 색으로 그리는 함수
def putPixel(x, y, pSize, pCol):               # 메인 소스 코드에서 호출하는 픽셀 채우기 함수
    turtle.penup()                             # 좌표 이동을 위해 펜기능을 비활성화   
    turtle.goto(x*pSize,(-1)*y*pSize)          # 주어진 좌표로 이동
    turtle.pendown()                           # 펜기능을 다시 활성화
    turtle.begin_fill()                        # 다각형을 그릴 때 내부를 채우기
    turtle.fillcolor(pCol)                     # 다각형의 채움색 설정하기
    turtle.setheading(45)                      # 시작 각도
    turtle.circle(pSize/2, steps = 4)          # 정사각형 픽셀 도출하기
    turtle.end_fill()                          # 채우기 끝
# -----------------------------------------------------------------------------

for j in range (0, 8) :                        #이미지의 행벡터(Xj)를 방문하기
    for i in range (0, 8) :                    # Xj의 각 성분 Xji를 하나씩 방문하기
        if (myImg[j][i] > 0):                  # 2차원 행렬 벡터 성분 Xji의 값을 확인하기
            putPixel(i,j,pixelSize, "blue")    # Xji > 0 인 경우 blue로 칠하기
        else:
            putPixel(i,j,pixelSize, "white")   # Xji <= 0 인 경우 흰색 칠하기


