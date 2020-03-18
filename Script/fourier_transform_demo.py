# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:45:36 2020

@author: Illusion
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

n = 1000
y = np.zeros(x.size)
for i in range(1, n + 1):
    y += 4 * np.pi / (2 * i - 1) * np.sin((2 * i - 1) * x)

complex_array = fft.fft(y)
print(complex_array.shape)  # (1000,) 
print(complex_array.dtype)  # complex128 
print(complex_array[0])  # (-2.1458390619955026e-12+0j)
y_new = fft.ifft(complex_array)

plt.subplot(311)
plt.grid(linestyle=':')
plt.plot(x, y, label='y')  # y是1000个相加后的正弦序列
plt.subplot(312)
plt.plot(x, y_new, label='y_new', color='orangered')  # y是ifft变换后的序列

# 得到分解波的频率序列
freqs = fft.fftfreq(x.size, x[1] - x[0])
# 复数的模为信号的振幅（能量大小）
complex_array = fft.fft(y)
pows = np.abs(complex_array)

plt.subplot(313)
plt.title('Frequency Domain', fontsize=16)
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Power', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.plot(freqs[freqs > 0], pows[freqs > 0], c='orangered', label='Frequency')
plt.legend()
plt.tight_layout()
plt.show()