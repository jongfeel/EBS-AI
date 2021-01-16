# 나만의 소리 파일의 샘플링 주기와 채널 타입 바꾸기

import numpy as np                                         # 행렬 및 벡터 데이터 관리를 위한 numpy 모듈
import matplotlib.pyplot as plt                            # 소리 데이터의 그래프 표현을 위한 모듈 
import scipy.io as sio            
from scipy.io.wavfile import write                         # wav 파일을 시스템 명령어로 재생하기 위한 모듈 
import os

# sampling rate
v_samplerate, v_data = sio.wavfile.read('thank_you.wav')
b_samplerate, b_data = sio.wavfile.read("Invisible_Beauty.wav")

v_times = np.arange(len(v_data))/float(v_samplerate)
b_times = np.arange(len(b_data))/float(b_samplerate)

# ------------------------------------------------------------------------

print(v_data.shape)
print(b_data.shape)
print(len(v_data))

# stereo channel -> mono channel
if (len(v_data.shape) > 1) : 
   v_data = np.array(v_data[:,0])
if (len(b_data.shape) > 1) :
   channel1 = np.array(b_data[:,0])
   channel2 = np.array(b_data[:,1])
   b_data = channel1 / 2 + channel2 / 2
   #b_data = np.array(b_data[:,0])

# 샘플링 주기 낮추기
if (v_samplerate > b_samplerate) :
   diffRate = v_samplerate / b_samplerate
   v_data = np.array(v_data[0:len(v_data):diffRate])
   sr = b_samplerate
elif (v_samplerate < b_samplerate) : 
   diffRate = int(b_samplerate / v_samplerate)
   b_data = np.array(b_data[0:len(b_data):diffRate])
   sr = v_samplerate
else :
   sr = b_samplerate

# 10초 지점의 배경 음악과 음성 데이터 합성하기
mix_data = v_data + b_data[sr*10:len(v_data)+sr*10]

# 합성한 데이터를 배경 음악 10초 위치에 넣기
b_data[sr*10:len(v_data)+sr*10] = mix_data

# 합성한 파일을 wav 파일로 저장하기
scaled = np.int16(b_data/np.max(np.abs(b_data)) * 32767)
write('music_card.wav', sr, scaled)
os.system("start music_card.wav")

