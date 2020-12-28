# 합성한 이미지 저장하기

# 외부 모듈 읽어오기
import numpy as np
import matplotlib.pyplot as plt 
import PIL.Image as pilimg                    # 이미지 처리를 하기 위한 외부 이미지

# image file 읽어오기
im1 = pilimg.open("jeju_summer.jpg")          # 배경 이미지 열기
im2 = pilimg.open("baby1.jpg")                # 조카 사진1  열기
im3 = pilimg.open("baby2.jpg")                # 조카 사2  열기

pix1 = np.array(im1)                          # image data를 numpy array로 구성
              
# 조카 사진을 이어붙이기 위해 배경에 맞추어 변경할 크기 계산하 
# 만약 배경 화면의 가로 크기가 홀수이면 첫번째 이미지의 가로 크기를 반올림하기
resizeX2 = pix1.shape[1]/2                    # 홀수인지 체크
if( pix1.shape[1] % 2 > 0) :                  # 홀수인 경우
    resizeX1 = pix1.shape[1]/2 + 1
else :
    resizeX1 = pix1.shape[1]/2                # 짝수인 경우


# 조카 사진 2장을 나란히 붙이기 위해 배경 이미지의 절반씩 차지하도록 크기 변경하기
im2 = im2.resize((int(resizeX1), int(pix1.shape[0])))     # 첫번째 조카 사진 크기 변경
pix2 = np.array(im2)

im3 = im3.resize((int(resizeX2), int(pix1.shape[0])))     # 두번째 조카 사진 크기 변경
pix3 = np.array(im3)

# 조카 사진 2개를 옆으로 나란히 붙이기(axis값을 0으로 하면 세로로 설정됨.)
pix4 = np.concatenate((pix2, pix3), axis = 1)             # 두 사진을 가로 방향으로 붙이기

# 이미지를 블렌딩하기 위해 각 픽셀의 RGB 값을 (0~1)의 실수 범위로 정규화(normalize)
pix1 = (1/255)*pix1
pix4 = (1/255)*pix4 

# 가중치 정하기(배경을 30%, 조카 이미지를 70%로 합성)
weight = 0.3

# 가중치를 적용하기 위해 원본 이미지 행렬에 가중치를 실수배하여 합하기
pix5 = pix1 * weight + pix4 * (1-weight)

# 두 원본 이미지의 가중치를 반대로 적용한 이미지 생성하기
pix6 = pix1 * (1-weight) + pix4 * weight

# ------------------------------------------------------------------------

pix5 = pix5*255
im5 = pilimg.fromarray(pix5.astype(np.uint8))
im5.save("BlendedPic_70.png")

pix6 = pix6*255
im6 = pilimg.fromarray(pix6.astype(np.uint8))
im6.save("BlendedPic_30.png")


