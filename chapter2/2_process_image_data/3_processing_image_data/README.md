# 이미지 데이터 가공하기

Review code

## 3-1 이미지 데이터 겹쳐 놓기

### 원본 이미지 파일 읽어오기

[2-2-07.py](2-2-07.py)

1 ~ 9 line 까지 단순히 준비된 이미지를 불러오는 코드

### 읽어온 두 이미지 합성하기

[2-2-07.py](2-2-07.py)

10 ~ 39 line 까지 이미지 합성 준비

np.array().shape() 함수의 의미: shape 함수는 어떤 행렬의 크기를 의미한다.

이미지파일을 읽어서 numpy array로 만들었는데, shape의 각각의 의미는 다음과 같다.

- shape[0]: image height
- shape[1]: image width
- shape[2]: RGB values

나머지는 책에 있는 설명과 코드의 주석만 잘 읽어도 이해할 수 있다.

### 합성한 이미지 출력하기

[2-2-07.py](2-2-07.py)

출력하는 코드는 이전 챕터에서 했던 것과 동일하다.

### 합성한 이미지 저장하기

[2-2-08.py](2-2-08.py)

np.unit8은 0 ~ 255의 범위를 가지는 type이므로 RGB 값의 범위에 맞는 type으로 변환한 후에 이미지로 저장한다.

## 3-2 컬러 이미지를 흑백 이미지로 만들기

[2-2-09.py](2-2-09.py)

코드는 어려운게 없지만 Luma에 대한 이해가 필요한 부분이다.

Luma=0.2126_R+0.7152_G+0.0722_B

[Relative_luminance](https://en.wikipedia.org/wiki/Relative_luminance)

에 대해 잘 보면 설명이 되어 있고 stack overflow에도 논의가 잘 된 글이 있다.

https://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color

