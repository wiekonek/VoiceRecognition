from __future__ import division #ok
from matplotlib import pylab as plt
import numpy as np
import scipy.io.wavfile
import random
import sys


def PrepareSignals(filename, beta=100):
    w, signal = scipy.io.wavfile.read(filename)
    if not isinstance(signal[0], np.int16):
        signal = [s[0] for s in signal]
    #transformata fourier'a
    spectrum = np.log(abs(np.fft.rfft(signal)))

    return w, signal, spectrum

def GetSex(fileName):
    try:
        w, signal = scipy.io.wavfile.read(fileName)
    except:
#         print("Cant open file: \"" + fileName + "\"")
        if random.randint(0, 1):
            return "K"
        else:
            return "M"
    else:
        w, signal, spectrum = PrepareSignals(fileName, 100)
        samplesCount = len(signal)
        time = samplesCount / w;

        maleSum = 0;
        femaleSum = 0;
        for maleFreqs in np.arange(85*time, 180*time):
            maleSum += spectrum[int(maleFreqs)]
        for femaleFreqs in np.arange(165*time, 255*time):
            femaleSum += spectrum[int(femaleFreqs)]

        if femaleSum > maleSum:
            return "K"
        else:
            return "M"

path = sys.argv[1]

print(GetSex(path))