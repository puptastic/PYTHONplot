import matplotlib.pyplot as plt
import numpy as np

print("Hello Python!\n\n")

t = np.arange(0.0, 2.0, 0.01)
v = 1 + np.sin(2*np.pi*t)
plt.plot(t, v)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('As simple as it gets, folks')
plt.grid(True)
# plt.savefig("test.png") # Just saving the figure as a picture in the same directory
plt.show()

print("Goodbye Python.")
