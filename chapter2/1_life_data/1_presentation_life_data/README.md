# 생활 데이터 표현하기

Review code and trouble shootings

## [Step 1] 유동 인구 데이터를 컴퓨터로 저장한 후 출력하기

제목은 거창하지만 array 출력하는게 전부인 코드, 컴퓨터로 저장한다는 개념이 array의 값들을 하드코딩하는 것이다.

[2-1-01.py](2-1-01.py)

``` python
# 은재가 조사한 일주일 간 유동인구 데이터 (월요일 ~ 일요일)
a = [242, 256, 237, 223, 263, 81, 46]     # 리스트에 유동 인구 데이터 초기화

print('A = ', a)                          # 출력하기
```

## [Step 2] 유동 인구수 데이터의 총합과 평균 구하기

Step 1에 이어서 유동인구 데이터의 합을 구하고 평균을 구한다. 여기까지는 프로그래밍을 모르고 수학 정도만 알고 있어도 이해가 가능하다.

[2-1-02.py](2-1-02.py)

python에는 sum() 함수를 쓸 수 있으므로 sum() 함수를 호출하여 간단하게 합을 구할 수 있다. 책에서는 for문의 동작 원리를 설명하려고 했기 때문에 for 문을 사용했다.

[2-1-02-sum.py](2-1-02-sum.py)

``` python
# 은재가 조사한 일주일 간 유동인구 데이터 (월요일 ~ 일요일)
a = [242, 256, 237, 223, 263, 81, 46]

# -----------------------------------------------------------
# 유동 인구 데이터의 총합과 평균 구하기

n = len(a)                          # 수열 a항 개수 구하기: 7개
my_sum = sum(a)                          # 합을 저장할 변수를 sum 함수를 호출하여 저장
my_avg = my_sum/n                   # 평균 구하기

print("Total Sum : ", my_sum)       # 총합 출력하기
print("Total Average : ", my_avg)   # 평균 출력하기
```

## [Step 3] 주어진 수열 데이터를 꺾은선 그래프로 표현하기

matplotlib라는 훌륭한 패키지를 이용해서 데이터 시각화를 할 수 있다.

[2-1-03.py](2-1-03.py)

맥북에서는 아마 맑은 고딕이 설치가 안되어 있을 수도 있고, 설치되어 있다고 하더라도 windows 기준으로 작성된 코드에서는 절대 맑은 고딕을 불러오기는 커녕 오류만 나게 된다.

다행히 다운로드 받은 소스코드에는 malgun.ttf 파일이 들어 있으므로 코드에 써 있는 malgun.ttf 파일 경로를 다음과 같이 상대 경로로 바꿔준다.

``` python
font_name = font_manager.FontProperties(fname="malgun.ttf").get_name()
```

그런데 이렇게 해도 폰트를 불러올 수가 없을 수도 있는데 이 경우는 맥북에 python 환경을 처음 설치해서 쓰는 경우일 것이다.

matplotlib의 font cache가 새로 설치했거나 혹은 코드에서 읽어들인 malgun.ttf 파일의 목록을 refresh하지 않았기 때문에 발생하는 것으로 구글 조금 검색해 보면 답을 찾을 수 있다.

python 코드로 입력하면 font_manager._rebuild()를 실행시켜 font cache를 refresh 해 준다.

``` python
font_manager._rebuild()
```

그러면 맥북에서도 아래 이미지 처럼 그래프를 볼 수 있다.

![2-1-03.png](2-1-03.png)

[2-1-03-iOS.py](2-1-03-iOS.py)

``` python
# 주어진 수열 데이터를 꺾은선 그래프로 표현하기

# 은재가 조사한 일주일 간 유동인구 데이터 (월요일 ~ 일요일)
a = [242, 256, 237, 223, 263, 81, 46]

# ----------------------------------------------------------------

# 그래프를 그리기 위한 외부 모듈 선언
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#한글을 출력하기 위한 폰트 로딩
font_name = font_manager.FontProperties(fname="malgun.ttf").get_name()
rc('font', family=font_name)                                    # 그래프 제목에 한글 표시하기
font_manager._rebuild()

x_data = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']       # x축에 표시할 제목 리스트에 저장 

# 그래프의 제목 붙이기 
plt.title("일주일간 유동 인구수 데이터", fontsize = 16)            # 큰 제목 
plt.xlabel("요일", fontsize=12)                                  # x축 제목
plt.ylabel("유동 인구수", fontsize=12)                           # y축 제목

plt.scatter(x_data, a)                                           # 꺽은선 그래프 그리기
plt.plot(x_data, a)
plt.show()
```

## [Step 4] 주중 유동 인구수의 합과 평균을 구해 그래프와 함께 출력하기

step2, step3의 내용을 잘 응용해서 원하는 데이터의 결과를 그래프로 출력한다.
iOS의 경우 step3에서 코드를 수정했으므로 step4의 코드도 같게 작성한다.

[2-1-04.py](2-1-04.py)

sum 값 구하는 방법은 step2에서 처럼 sum 함수를 이용하는 방식으로 구한다.

[2-1-04-sum.py](2-1-04-sum.py)

``` python
# 주중 유동 인구만으로 합과 평균을 구해 그래프와 함께 출력하기

# 은재가 조사한 일주일 간 유동 인구 데이터 (월요일 ~ 일요일)
a = [242, 256, 237, 223, 263, 81, 46]

# 그래프를 그리기 위한 외부 모듈 읽어들이기
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#한글을 출력하기 위한 폰트 로딩
font_name = font_manager.FontProperties(fname="malgun.ttf").get_name()
rc('font', family=font_name)

x_data = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN'] # x축에 표시할 문구

# -----------------------------------------------------------
# 주중 데이터만으로 합과 평균 구하기
weekday_size = 5                           # 주중이므로 5
weekday_sum = 0                            # 합이 저장될 변수 초기화   
weekday_avg = 0                            # 평균이 저장될 변수 초기화

weekday_sum = sum(a[:weekday_size])        # 주중 유동 인구 총합 구하기 
weekday_avg = weekday_sum/weekday_size     # 주중 유동 인구 평균 구하기

# 계산한 총합과 평균 출력하기
print("weekday Data = ", a[0:5])           # 주중 데이터 출력하기
print("weekday Sum : ", weekday_sum)       # 합 출력
print("weekday Average : ", weekday_avg)   # 평균 출력

# 그래프의 제목 붙이기 
plt.title("주중 유동 인구수 데이터", fontsize = 16)   # 큰 제목
plt.xlabel("요일", fontsize=12)                     # x축 제목 
plt.ylabel("유동 인구수", fontsize=12)              # y축 제목

# 꺽은선 그래프 그리기 
plt.plot(x_data, a)
plt.scatter(x_data[0:weekday_size], a[0:weekday_size], c = 'red', edgecolor = 'none', s = 50)

plt.show()

```