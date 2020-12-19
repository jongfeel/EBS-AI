# 여러 색을 갖는 이미지 데이터 표현하기

# 외부 모듈 정의
import numpy as np                  # 벡터, 행렬 데이터를 쉽게 처리하기 위한 모듈
import matplotlib.pyplot as plt     # 화면에 이미지 데이터를 보여주기 위한 모듈 
import PIL.Image as pilimg          # 이미지 파일과 데이터 처리를 위한 모듈

im = pilimg.open( "rgb_circle.bmp" ) # image file 읽어오기 

pix = np.array(im)                   # image data를 numpy array로 구성하기
pixSize = np.array(pix.shape)
print(pixSize)

# pix array에서 각각 R(0), G(1), B(1) 성분 값 외에는 0으로 만들어서
# 원본 이미지에서 R, G, B에 해당하는 배열 만들기 
pix_R = pix.copy()
pix_R[:, :, (1,2)] = 0
pix_G = pix.copy()
pix_G[:, :, (0,2)] = 0
pix_B = pix.copy()
pix_B[:, :, (0,1)] = 0

# 원본 이미지인 pix 행렬을 이미지 데이터로 출력
plt.subplot(141)
plt.imshow(pix)
plt.axis("off")
plt.title("RGB")

# pix 행렬에서 이미지 데이터의 R 채널을 출력
plt.subplot(142)
plt.imshow(pix_R)
plt.axis("off")
plt.title("R(Red)")

# pix 행렬에서 이미지 데이터의 G 채널을 출력
plt.subplot(143)
plt.imshow(pix_G)
plt.axis("off")
plt.title("G(Green)")

# pix 행렬에서 이미지 데이터의 B 채널을 출력
plt.subplot(144)
plt.imshow(pix_B)
plt.axis("off")
plt.title("B(Blue)")
plt.show()
 
