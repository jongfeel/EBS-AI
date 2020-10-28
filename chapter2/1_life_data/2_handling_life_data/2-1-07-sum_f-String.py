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
    print(f'[~{hour_value}:00]: {int(avgh[hour_index]):4}')     # 시간대별 유동 인구수 출력