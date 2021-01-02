# 소리 데이터에 필요한 외부 모듈 설정하기

# 소리 파일을 다루기 위한 모듈
import numpy as np                                    # 행렬 및 벡터 데이터 관리를 위한 numpy 모듈
import matplotlib.pyplot as plt                       # 음성 데이터의 그래프 표현을 위한 모듈
                             
import scipy.io.wavfile 
import sounddevice as sd                              # 소리 데이터를 실제 스피커로 출력하기 위한 사운드 장치 모듈


# 작업 폴더에 저장된 ‘thank_you.wav’ 파일 읽기
v_samplerate, v_data = scipy.io.wavfile.read("thank_you.wav")
times = np.arange(len(v_data))/float(v_samplerate)     # x축 시간 정보를 구하기

print('sampling rate: ', v_samplerate)                 # wav 파일의 샘플링 주기를 출력
print('time : ', times[-1])                            # 소리의 재생 시간을 출력(times[ ]의 마지막 성분의 값)
print('vData : ', v_data[5000:5100])                   # 5000번째 샘플링 데이터부터 100개를 출력
sd.play(v_data, v_samplerate)                          # 읽어 들인 wav 파일을 사운드 장치로 출력

# wav 형식의 소리 데이터를 그래프로 출력(X축: 소요 시간, Y축: 소리의 높낮이 진폭값)
plt.plot(times, v_data)
plt.xlim(times[0], times[-1])
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.show()

