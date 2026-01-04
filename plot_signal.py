import numpy as np
import matplotlib.pyplot as plt

# Fake ECG-like signal (for learning)
t = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 5 * t) + 0.2 * np.random.randn(len(t))

plt.plot(t, signal)
plt.title("Fake ECG Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
