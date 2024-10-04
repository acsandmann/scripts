import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * np.sin(x)

x_vals = np.linspace(-10, 10, 400)

y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label=r'$f(x) = x \sin(x)$')
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.title(r'Graph of $f(x) = x \sin(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()