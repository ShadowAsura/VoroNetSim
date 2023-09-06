import numpy as np
import matplotlib.pyplot as plt

# Generate a sample sine wave signal
# We'll use a frequency of 5 Hz and sample it at 1000 samples per second
fs = 1000  # Sampling rate (samples per second)
t = np.linspace(0, 1, fs, endpoint=False)  # Time array
f = 5  # Frequency of the sine wave (Hz)
x = 0.5 * np.sin(2 * np.pi * f * t)  # Sampled sine wave signal

# Perform Fourier Transform using numpy's fft function
# This will give us the frequency components of the signal
X = np.fft.fft(x)

# Generate frequency bins for plotting
frequencies = np.fft.fftfreq(len(X), 1/fs)

# Plot the original signal
plt.figure()
plt.subplot(2, 1, 1)
plt.title("Original Signal")
plt.plot(t, x)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Plot the magnitude of the Fourier Transform
plt.subplot(2, 1, 2)
plt.title("Fourier Transform")
plt.plot(frequencies, np.abs(X))
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")

# Show plots
plt.show()
