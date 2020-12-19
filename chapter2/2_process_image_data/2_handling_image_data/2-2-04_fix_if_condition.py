# 행렬의 합을 이용해서 두 이미지를 결합하기
# 외부 모듈 선언
import turtle
import numpy as np

pixelSize = 10

def putPixel(x, y, pSize, pCol):        # 메인 소스 코드에서 호출하는 Pixel 채우기 함수
    turtle.penup()                      # 좌표 이동을 위해 펜기능을 비활성화
    turtle.goto(x*pSize,(-1)*y*pSize)   # 주어진 좌표로 이동
    turtle.pendown()                    # 펜기능을 다시 활성화
    turtle.begin_fill()                 # 다각형을 그릴 때 내부를 채우기
    turtle.fillcolor(pCol)              # 다각형의 채움색 설정하기
    turtle.setheading(45)               # 시작각도
    turtle.circle(pSize/2, steps = 4)   # 정사각형 픽셀 그리기
    turtle.end_fill()                   # 채우기 끝

faceImg = np.array(                                       # 46쪽 (a) 도형을 나타내는 이미지 데이터 행렬 
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

smileImg = np.array(                                     # 46쪽 (b) 도형을 나타내는 이미지 데이터 행렬
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# ---------------------------------------------------------------------------------------------------    
addImage = np.array(faceImg + smileImg)              # faceImg 행렬과 smailImage 행렬의 합
print(addImage)                                      # addImg의 성분 출력하기

# 원래 이미지 2개의 합으로 새로 생성된 이미지 데이터 행렬 addImage를 출력하기
for j in range (0, 16) : 
    for i in range (0, 16) :
        if (addImage[j][i] >= 2) :                     # addImage 행렬의 성분값이 2 이상이면 빨간색으로 출력하기
            putPixel(i,j,pixelSize, "red")
        elif (addImage[j][i] == 1) :                   # addImage 행렬의 성분값이 1이면 오렌지색으로 출력하기
            putPixel(i,j,pixelSize, "orange")        
        else :                                        # ddImage 행렬의 성분값이 0 이하이면 흰색으로 출력하기
            putPixel(i,j,pixelSize, "white")         
