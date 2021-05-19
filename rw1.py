import numpy as np
import matplotlib.pyplot as plt

def u(t):
    return np.array(t >= 0, dtype=np.int)

n = np.arange(10, 40, 1)
n1 = 20     
n2 = 26

_u = u(n-n1) - u(n-n2)

plt.stem(n, _u, use_line_collection=True)
plt.title(u'u[n-20] - u[n-26]')

plt.show()