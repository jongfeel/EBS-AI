# 내가 만약 축구팀 감독이라면

Review code

## 데이터 수집하기

제목은 거창하지만 csv 파일에 축구 선수 데이터가 있다는 소개

### 생각해 보기

> 여러 가지 데이터 중 게임 사용자가 가장 중요하게 생각하는 요소를 반영하여 데이터를 분석하려면 어떻게
해야 하는지 생각해 보자

먼저 csv 파일에 들어 있는 메타 데이터가 무엇인지 살펴봐야 한다.

ID	Name	Age	Photo	Nationality	Flag	Overall	Potential	Club	Club Logo	Value	Wage	Special	Preferred Foot	International Reputation	Weak Foot	Skill Moves	Work Rate	Body Type	Real Face	Position	Jersey Number	Joined	Loaned From	Contract Valid Until	Height	Weight	LS	ST	RS	LW	LF	CF	RF	RW	LAM	CAM	RAM	LM	LCM	CM	RCM	RM	LWB	LDM	CDM	RDM	RWB	LB	LCB	CB	RCB	RB	Crossing	Finishing	HeadingAccuracy	ShortPassing	Volleys	Dribbling	Curve	FKAccuracy	LongPassing	BallControl	Acceleration	SprintSpeed	Agility	Reactions	Balance	ShotPower	Jumping	Stamina	Strength	LongShots	Aggression	Interceptions	Positioning	Vision	Penalties	Composure	Marking	StandingTackle	SlidingTackle	GKDiving	GKHandling	GKKicking	GKPositioning	GKReflexes	Release Clause

이렇게나 많은 데이터를 표현해 주고 있다.

만약 이게 게임 데이터로 써야 한다면 실질적으로 선수들의 능력치를 중요하게 봐야 할 것 같고 그렇다면 `Overall`, `Potential`의 종합적인 수치와 포지션별 능력치인 `Crossing Finishing` 부터 시작하는 능력치 중 내가 선호하는 능력치가 월등한 선수를 선발해야 한다.

최대값이나 평균값을 얻어 그 점수가 좋은 선수를 선발한다면 의미가 있을 것이다.

## 데이터 불러오기

### 파일에 저장한 데이터를 불러와 출력하기

[3-1-01.py](3-1-01.py)

``` python
# 파일에 저장한 데이터를 불러와 출력하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')        # fifa2019.csv 파일의 데이터 불러오기

print(fifa2019.shape)                         # 출력하기
```

pandas를 사용하면 csv 파일을 쉽게 읽어올 수 있다.

shape의 출력값은 (18207, 89)인데 row 18207, col 89라는 뜻이다. col 89개가 뭐가 있는지는 생각해보기에서 이미 살펴봤다.

### fifa2019에 저장된 개별 값들을 열별로 확인하기

[3-1-02.py](3-1-02.py)

``` python
# fifa2019에 저장된 개별 값들을 열별로 확인하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

# --------------------------------------------

print(fifa2019.info())
```

csv 파일 정보를 출력

<details>
<summary>fifa.2019.info() 출력값 펼쳐보기</summary>
<p>

``` shell
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 18207 entries, 0 to 18206
Data columns (total 89 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   Unnamed: 0                18207 non-null  int64  
 1   ID                        18207 non-null  int64  
 2   Name                      18207 non-null  object 
 3   Age                       18207 non-null  int64  
 4   Photo                     18207 non-null  object 
 5   Nationality               18207 non-null  object 
 6   Flag                      18207 non-null  object 
 7   Overall                   18207 non-null  int64  
 8   Potential                 18207 non-null  int64  
 9   Club                      17966 non-null  object 
 10  Club Logo                 18207 non-null  object 
 11  Value                     18207 non-null  object 
 12  Wage                      18207 non-null  object 
 13  Special                   18207 non-null  int64  
 14  Preferred Foot            18159 non-null  object 
 15  International Reputation  18159 non-null  float64
 16  Weak Foot                 18159 non-null  float64
 17  Skill Moves               18159 non-null  float64
 18  Work Rate                 18159 non-null  object 
 19  Body Type                 18159 non-null  object 
 20  Real Face                 18159 non-null  object 
 21  Position                  18147 non-null  object 
 22  Jersey Number             18147 non-null  float64
 23  Joined                    16654 non-null  object 
 24  Loaned From               1264 non-null   object 
 25  Contract Valid Until      17918 non-null  object 
 26  Height                    18159 non-null  object 
 27  Weight                    18159 non-null  object 
 28  LS                        16122 non-null  object 
 29  ST                        16122 non-null  object 
 30  RS                        16122 non-null  object 
 31  LW                        16122 non-null  object 
 32  LF                        16122 non-null  object 
 33  CF                        16122 non-null  object 
 34  RF                        16122 non-null  object 
 35  RW                        16122 non-null  object 
 36  LAM                       16122 non-null  object 
 37  CAM                       16122 non-null  object 
 38  RAM                       16122 non-null  object 
 39  LM                        16122 non-null  object 
 40  LCM                       16122 non-null  object 
 41  CM                        16122 non-null  object 
 42  RCM                       16122 non-null  object 
 43  RM                        16122 non-null  object 
 44  LWB                       16122 non-null  object 
 45  LDM                       16122 non-null  object 
 46  CDM                       16122 non-null  object 
 47  RDM                       16122 non-null  object 
 48  RWB                       16122 non-null  object 
 49  LB                        16122 non-null  object 
 50  LCB                       16122 non-null  object 
 51  CB                        16122 non-null  object 
 52  RCB                       16122 non-null  object 
 53  RB                        16122 non-null  object 
 54  Crossing                  18159 non-null  float64
 55  Finishing                 18159 non-null  float64
 56  HeadingAccuracy           18159 non-null  float64
 57  ShortPassing              18159 non-null  float64
 58  Volleys                   18159 non-null  float64
 59  Dribbling                 18159 non-null  float64
 60  Curve                     18159 non-null  float64
 61  FKAccuracy                18159 non-null  float64
 62  LongPassing               18159 non-null  float64
 63  BallControl               18159 non-null  float64
 64  Acceleration              18159 non-null  float64
 65  SprintSpeed               18159 non-null  float64
 66  Agility                   18159 non-null  float64
 67  Reactions                 18159 non-null  float64
 68  Balance                   18159 non-null  float64
 69  ShotPower                 18159 non-null  float64
 70  Jumping                   18159 non-null  float64
 71  Stamina                   18159 non-null  float64
 72  Strength                  18159 non-null  float64
 73  LongShots                 18159 non-null  float64
 74  Aggression                18159 non-null  float64
 75  Interceptions             18159 non-null  float64
 76  Positioning               18159 non-null  float64
 77  Vision                    18159 non-null  float64
 78  Penalties                 18159 non-null  float64
 79  Composure                 18159 non-null  float64
 80  Marking                   18159 non-null  float64
 81  StandingTackle            18159 non-null  float64
 82  SlidingTackle             18159 non-null  float64
 83  GKDiving                  18159 non-null  float64
 84  GKHandling                18159 non-null  float64
 85  GKKicking                 18159 non-null  float64
 86  GKPositioning             18159 non-null  float64
 87  GKReflexes                18159 non-null  float64
 88  Release Clause            16643 non-null  object 
dtypes: float64(38), int64(6), object(45)
memory usage: 12.4+ MB
None
```

</p>
</details>

## 데이터 다루기

전반적으로 pandas 사용 예제 정도이다. 코드만 보고도 이해할 수 있는 수준이므로 코드만 언급하고 넘어간다.

### 궁금한 선수의 데이터 검색하기

[3-1-03.py](3-1-03.py)

``` python
# 궁금한 선수의 데이터 검색하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

# --------------------------------------------

sub1 = fifa2019.loc[14]      # fifa2019의 인덱스 레이블 14인 행값을 sub1에 저장
print(sub1)
```

pandas loc 함수는 아래 링크를 참고한다.

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html

### 원하는 범위의 데이터 검색하기

[3-1-04.py](3-1-04.py)

``` python
# 원하는 범위의 데이터 검색하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

# ---------------------------------------------

sub2 = fifa2019.loc[2:16]                        # 인덱스 레이블 2부터 16까지인 행 값을 sub2에 저장하기
print(sub2)
```

### 전체 선수들의 이름과 선호하는 발 정보 출력하기

[3-1-05.py](3-1-05.py)

``` python
# 전체 선수들의 이름과 선호하는 발 정보 출력하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

# ----------------------------------------------------

sub3 = fifa2019.loc[:,['Name', 'Preferred Foot']]
print(sub3)
```

콜론(:)은 이제 전체 row를 가져온다는 건 자연스럽게 알 수 있고, 뒤에 col 부분에 필요한 label을 적어 주면 예상한 대로의 결과 값을 얻을 수 있다.

### 여러 행의 데이터 중 원하는 열 값만 골라 출력하기

[3-1-06.py](3-1-06.py)

``` python
# 여러 행의 데이터 중 원하는 열 값만 골라 출력하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

# ------------------------------------------------

sub4 = fifa2019.iloc[0:10,1:3]         # 0~9행, 1, 2열값을 sub4에 저장하기
print(sub4)
```

### 우리나라 선수들 출력하기

[3-1-07.py](3-1-07.py)

``` python
# 우리나라 선수들 출력하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

# ---------------------------------------------------------

korea_player=fifa2019['Nationality']=='Korea Republic'

sub5 = fifa2019.loc[korea_player]

print(korea_player)
print(sub5)
```

여기서 `sub5 = fifa2019.loc[korea_player]` 이 부분이 흥미로운데
실제 출력을 해 보면 True, False의 값들로 이루어진 array가 출력되는 걸 알 수 있다.

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html

다시 loc 함수의 문서를 잘 보면

Access a group of rows and columns by label(s) or a boolean array.

이라고 되어 있다.

즉 label이나 boolean array를 가지고 데이터를 가져올 수 있다는 뜻이다.

### 우리나라 선수들의 이름 출력하기

[3-1-08.py](3-1-08.py)

``` python
# 우리나라 선수들의 이름 출력하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

korea_player=fifa2019['Nationality']=='Korea Republic'
sub5 = fifa2019.loc[korea_player]

# ------------------------------------------------------------

sub6 = sub5['Name']
print(sub6)
```

## 데이터 시각화하기

### 선수들이 선호하는 발의 종류 데이터를 막대그래프로 나타내기

[3-1-09.py](3-1-09.py)

``` python
# 선수들이 선호하는 발의 종류 데이터를 막대그래프로 나타내기

import pandas as pd                      # 그래프를 출력하기 위한 모듈  

fifa2019 = pd.read_csv('fifa2019.csv')

# --------------------------------------------------------------------

import matplotlib.pyplot as plt          # 그래프를 출력하기 위한 모듈

fifa2019['Preferred Foot'].value_counts().plot(kind='bar')
plt.legend()                             # 범례 표시하기
plt.show()                               # 그래프 출력하기
```

pandas에서 바로 plot으로 그래프 데이터를 통해 그래프를 그리는 함수가 자연스럽다.

``` python
plt.plot(...)
```

여태까지는 이런 코드로 그래프에 그려질 데이터를 넣는게 자연스러웠지만 이번 코드는 데이터가 준비가 되었다는 가정, 그리고 matplotlib이 import가 되었다는 가정하에 연동되는 함수라고 보면 된다.

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.plot.html

pandas api에도 `By default, matplotlib is used.`로 되어 있다.

또한 legend를 표시할 거라면 plot 파라미터에 legend=True를 주면 별도로 plt.legend()를 호출할 필요가 없다.

``` python
fifa2019['Preferred Foot'].value_counts().plot(kind='bar', legend=True)
#plt.legend()                             # 범례 표시하기, 이제 필요 없음
plt.show()   
```

### 선수들이 선호하는 발의 종류를 원 그래프로 나타내기

[3-1-10.py](3-1-10.py)

``` python
# 선수들이 선호하는 발의 종류를 원 그래프로 나타내기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

import matplotlib.pyplot as plt         # 그래프를 출력하기 위한 모듈

# ---------------------------------------------------------------------

fifa2019['Preferred Foot'].value_counts().plot(kind='pie', autopct='%1.f%%')
plt.legend()                            # 범례 표시하기
plt.show()                              # 그래프 출력하기
```

같은 데이터를 파이 그래프로 그린다. autopct의 경우는 책에도 설명이 잘 나와 있지만, 역시 표현하는 방법은 공식 문서를 확인하는게 도움이 된다. 라고 생각했지만 설명이 좀 부실하다. 그래서 만약 더 찾아보고 싶으면 검색해서 다른 사람들의 블로그를 참고해 보면 좋다.

https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.pie.html
