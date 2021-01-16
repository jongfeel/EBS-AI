# 생활 속의 소리 합성하기

import numpy as np                                         # 행렬 및 벡터 데이터 관리를 위한 numpy 모듈
import matplotlib.pyplot as plt                            # 소리 데이터의 그래프 표현을 위한 모듈 

import scipy.io as sio                                     # wav 형식으로 소리 데이터를 저장하기 위한 모듈                         
from scipy.io.wavfile import write                         # wav 파일을 시스템 명령어로 재생하기 위한 모듈 
import os

# sampling rate
Fs = 44100.0                                   # 정보 샘플링 주기, 1초에 44100개의 샘플링, 단위는 Hz(주파수)            

# 1초 데이터 생성을 위한 환경 변수 설정
tlen = 1                                       # 1초
Ts = 1/Fs                                      # 샘플링 사이의 간격(시간)
t = np.arange(0, tlen, Ts)                     # 소리 데이터를 생성할 시간 성분으로 구성된 배열로
                                               # [0, 1] 사이를 TimeStamp의 간격으로 분할하여
                                               # Fs 개의 데이터를 담을 수 있는 배열 t를 생성
                                               
# 시그널 생성하기
sin_freq = 440                                 # sin 곡선의 주기
src = 2*np.pi*sin_freq*t                       # t 배열의 각 성분값에 sin 주기를 라디안 단위로 변환한 src 배열을 준비
signal = np.sin(src)                           # timestamp를 각으로 변환한 src 배열에 맞게 sin 데이터를 변환


# 데이터의 가시화: 생성한 시그널 데이터를 그래프로 표현
x_range = 200                                  # 시작부터 200개의 데이터만 보여 주기 위한 범위값
noise = np.random.uniform(-1, 1, len(t))       # 균등분포의 난수로 구성된 잡음 데이터 생성

# -----------------------------------------------------------------------------------------
signal_n = signal + noise

# signal + noise로 두 소리 데이터를 산술적으로 더함.
scaled_noise = noise * 0.3                     # 소리 크기를 30% 줄이기
signal_n = signal + scaled_noise
# save as wav file
scaled = np.int16(signal_n/np.max(np.abs(signal_n)) * 32767)
write('snd_noise.wav', 44100, scaled)

#show the raw signals
plt.plot(t[0:x_range], signal[0:x_range], color = 'blue')
plt.plot(t[0:x_range], scaled_noise[0:x_range], color = 'red')
plt.show()

plt.plot(t[0:x_range], signal_n[0:x_range], color = 'green')
plt.show()


