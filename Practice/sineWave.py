import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1          # Amplitude
f = 5          # Frequency (Hz)
Fs = 1000      # Sampling frequency (Hz)

# Time axis
t = np.arange(0, 1, 1/Fs)

# Sine wave
x = A * np.sin(2 * np.pi * f * t)

# Plot
plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave")
plt.grid()
plt.show()