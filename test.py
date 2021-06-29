import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data/data')

x, y, z = [], [], []
for r in data:
  x += list(r[0::3])
  y += list(r[1::3])
  z += list(r[2::3])

plt.plot(x)
plt.plot(y)
plt.plot(z)
plt.grid()
plt.show()
