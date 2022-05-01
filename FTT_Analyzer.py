import numpy as np 
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt
import math

BUFFER = 1500
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100 #Hz

p = pa.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = BUFFER
)

# FFT

#FFT line change
data = stream.read(BUFFER)
dataInt = struct.unpack(str(BUFFER) + 'h', data)
fft_data = np.abs(np.fft.fft(dataInt))*2/(11000*BUFFER)


# FTT Frequency tracking
# freqs = np.fft.fftfreq(len(np.fft.fft(dataInt)))
# for idx, freq in enumerate(freqs[:len(freqs)]):
#     print("Freq:", int(abs(freq * RATE)), end='' )
#     # print(" Pwer:", fft_data[0])
#     print("\n")
    
# print("Freq:", int(abs(freqs[len(freqs)//165] * RATE)))

while True:
    # Audio Data Input 
    data = stream.read(BUFFER)
    dataInt = struct.unpack(str(BUFFER) + 'h', data)
    fft_data = np.abs(np.fft.fft(dataInt))*2/(11000*BUFFER)
   

    # FFT Plotting
    
    highFreqs = round(np.mean( fft_data[(len(fft_data)//35):(len(fft_data)-1)//2] ),3) 

    midFreqs = round(np.mean( fft_data[(len(fft_data)//165):(len(fft_data)//40)] ),3) 

    lowFreqs = round(np.mean( fft_data[0:(len(fft_data)//185)] ),3) 

    if highFreqs >= 0.002 and highFreqs != 0.0:
        print("High: ", highFreqs)

    if midFreqs >= 0.02 and midFreqs != 0.0:
        print("Mid: ", midFreqs)
        
    if lowFreqs >= 0.1 and lowFreqs != 0.0: 
        print("Low: ", lowFreqs)


    # specific frequency testing

    # if round(fft_data[1], 3) > 0.0 and round(fft_data[1], 3) != 0.0: 
    #    print("freq: ", int(abs(freqs[1] * RATE))," Power:", round(fft_data[1], 3))
