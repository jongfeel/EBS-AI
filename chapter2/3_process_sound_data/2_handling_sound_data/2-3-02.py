# 소리 데이터에 필요한 외부 모듈과 환경 변수 설정하기

import numpy as np                             # 행렬 및 벡터 데이터 관리를 위한 numpy 모듈
import matplotlib.pyplot as plt                # 소리 데이터의 그래프 표현을 위한 모듈
from scipy.io.wavfile import write             # wav 형식으로 소리 데이터를 저장하기 위한 모듈
import os                                      # wav 파일을 시스템 명령어로 재생하기 위한 모듈

# sampling rate
Fs = 44100.0                                   # 정보 샘플링 주기, 1초에 44100개의 샘플링, 단위는 Hz(주파수)            

# 1초 데이터 생성을 위한 환경 변수 설정
tlen = 1                                       # 1초
Ts = 1/Fs                                      # 샘플링 사이의 간격(시간)
t = np.arange(0, 1, 1/44100.0)                 # 소리 데이터를 생성할 시간 성분으로 구성된 배열로
                                               # [0, 1] 사이를 TimeStamp의 간격으로 분할하여
                                               # Fs 개의 데이터를 담을 수 있는 배열 t를 생성
                                               
# 시그널 생성하기
sin_freq = 440                                 # sin 곡선의 주기
src = 2*np.pi*sin_freq*t                       # t 배열의 각 성분값에 sin 주기를 라디안 단위로 변환한 src 배열을 준비
signal = np.sin(src)                           # timestamp를 각으로 변환한 src 배열에 맞게 sin 데이터를 변환

# 데이터의 가시화: 생성한 시그널 데이터를 그래프로 표현
x_range = 200                                  # 시작부터 200개의 데이터만 보여 주기 위한 범위값
plt.plot(t[0:x_range], signal[0:x_range], color = 'blue')    # x축의 timstamp에 sin 함수로 생성한 데이터를 y축에 좌푯값으로 그래프를 그림

plt.show()                                     # 200개의 데이터를 가시화한 그래프를 보여줌.

# 데이터의 가시화: 시그널 데이터를 푸리에 변환하여 주파수 영역에서 가시화함.
freq = np.fft.fftfreq(len(t), Ts)              # 주파수 영역에서의 샘플링 구간값의 배열
signal_f = np.fft.fft(signal)                  # sin 함수값으로부터 주파수 영역에서의 정보를 나타내기
                                               # 위한 푸리에 변환 값을 signal_f 배열로 저장
plt.plot(freq[0:x_range], 20*np.log10(np.abs(signal_f[0:x_range])), color='blue')
                                               # x축의 주파수 성분에 맞게 그래프를 그림.
plt.show()                                     # 푸리에 변환된 200개 데이터를 그래프로 출력

# sin 함수로 생성한 음성 데이터를 wav 형식의 파일로 저장
#scaled = np.int16(signal/np.max(np.abs(signal)) * 32767)
#write('snd_signal.wav', 44100, scaled)

