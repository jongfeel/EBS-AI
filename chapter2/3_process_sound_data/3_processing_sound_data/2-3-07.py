# 나만의 소리 파일의 데이터와 샘플링 주기 확인하기

import numpy as np                                         # 행렬 및 벡터 데이터 관리를 위한 numpy 모듈
import scipy.io as sio                                   
from scipy.io.wavfile import write                         # wav 파일을 시스템 명령어로 재생하기 위한 모듈 
import os

# sampling rate
v_samplerate, v_data = sio.wavfile.read("thank_you.wav")
b_samplerate, b_data = sio.wavfile.read("Invisible_Beauty.wav")

v_times = np.arange(len(v_data))/float(v_samplerate)
b_times = np.arange(len(b_data))/float(b_samplerate)

print('sampling rate: ', v_samplerate, b_samplerate)
print('time : ', v_times[-1], b_times[-1])
print('len : ', len(v_data), len(b_data))

print(v_data.shape)
print(b_data.shape)

