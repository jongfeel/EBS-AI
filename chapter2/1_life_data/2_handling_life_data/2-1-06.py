# 파일로 저장된 데이터 불러오기

import csv                                                  # csv 파일을 읽어들이기 위한 패키지 

a = [[],[],[],[],[],[],[]]                                  # 7 x 24 크기의 리스트 선언

with open('passby_data.csv', 'r') as f :                    # 데이터가 저장된 csv 파일 열기
    reader = csv.DictReader(f)
    i = j = 0                                               # i, j 변수 선언 및 초기화
    for row in reader :                                     # 데이터 수만큼 반복        
        a[i].append(row)                                    # 리스트 a에 읽은 데이터 저장
        j = j + 1
        if(j % 24 == 0) :                                   # 다음 요일로 이동 여부를
            i = i + 1                                       # 판단하기 위한 조건문

x_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']  # 요일 제목 저장

for i in range (0, 7) :                                      # 월~일요일까지 7번 반복
    
    for j in range (0, len(a[i])) :                          # 데이터 수만큼 반복
        
        print(x_title[i], "[", j, "] = ", a[i][j])           # 시간대별로 데이터 출력    
        
