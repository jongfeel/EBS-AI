# 생활 데이터 다루기

Review code and trouble shootings

## 데이터를 직접 설정하기

리스트에 딕셔너리 형태의 데이터를 하드코딩으로 추가하고 출력해 보기, 사실 csv 파일에서 읽어들이는게 편한 방법이라는 걸 설명하기 위해 일부러 어려운 방법을 코드로 보여준 듯

[2-1-05.py](2-1-05.py)

## 파일로 저장된 데이터 불러오기

본격적으로 csv 파일을 불러오는 작업을 진행한다.

[2-1-06.py](2-1-06.py)

## 데이터로부터 시간대별 평균 유동 인구수 구하기

여기서 부터 원하는 데이터를 추려서 가져오는 방법에 대한 코드가 나온다.

[2-1-07.py](2-1-07.py)

주석도 그렇고 코드가 매우 가독성이 떨어진다. 그래서 아래 네가지 포인트로 리팩토링 한다.

- csv 파일 읽는 부분에서 i, j 사용으로 인한 가독성 해소 => day, hour 변수 이름 사용
- enumerate 함수를 통해 요일과 시간 array의 index 확보 => 24, 7과 같은 magic number 배제
- python 3.6 부터 사용 가능한 [f-string](https://www.python.org/dev/peps/pep-0498/?) 문법으로 직관적인 string formatting 문법 사용
- 평균 값을 구한 후에 또 다시 for문을 돌려 출력하지 않고 평균 값을 구한 뒤 바로 출력, for문 두 번 돌리는 낭비를 방지함

[2-1-07-sum_f-String.py](2-1-07-sum_f-String.py)

``` python
# 데이터로부터 시간대별 평균 유동 인구수 구하기

import csv

a = [[],[],[],[],[],[],[]]                     # 7 x 24 크기의 리스트 선언

# a[i] = dictionary {num, wnum, ynum} : 요일별로 각 시간대에 저장할 데이터
# csv 파일에서 데이터를 읽어서 2차원 배열 a[][]에 저장 
with open('passby_data.csv', 'r') as f :
    reader = csv.DictReader(f)
    day = hour =  0
    for row in reader :        
        a[day].append(row)
        hour += 1
        if(hour % 24 == 0) :                       # 24개 데이터 읽었으면 다음 요일로 넘어가기 
            day += 1

# -------------------------------------------------------------------------

day_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']     # 요일 제목
hour_title = ['01', '02', '03', '04', '05', '06', \
              '07', '08','09', '10', '11', '12', \
              '13', '14','15', '16', '17', '18', \
              '19', '20','21', '22', '23', '24',]


# 시간대별로 주간 평균값 구하기
avgh = []
for hour_index, hour_value in enumerate(hour_title) :                          # 0~23시간만큼 19~24행 반복                     
    day_sum = 0                                  # 시간대별 합을 구하기 위해 0으로 초기화
    # 각 시간대 주간 총합
    for day_index, day_value in enumerate(day_title) :                      # 일주일, 즉 7번 반복하기
        day_sum += int(a[day_index][hour_index]['num'])  # 요일별 + 시간대별 행인수 누적하기

    avgh.append(day_sum/7)                       # 시간대 주간 행인수 평균 구하기
    print(f'[~{hour_value}:00]: {int(avgh[hour_index]):4}')     # 시간대별 유동 인구수 출력, :4의 경우는 앞자리 공백 4칸을 채우고 숫자 출력, 오른쪽 정렬의 효과를 가진다.
```