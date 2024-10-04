import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return -0.3*x**3 + 0.5*x**2 - 0.1*x - 0.2

def tangent_line(x):
    slope = 1.5
    return slope * (x + 0.25) - 0.186

x_vals = np.linspace(-3, 3, 400)

plt.plot(x_vals, f(x_vals), label='f(x)', color='red')

x_tangent = np.linspace(-3, 3, 400)
plt.plot(x_tangent, tangent_line(x_tangent), label="Tangent at x = -0.25", linestyle="--")

plt.scatter([-0.25, 0.5, 1.5], [-0.186, -0.594, 0.394], color="black", zorder=5)
plt.text(-0.25, -0.186, "(-0.25, -0.186)", fontsize=9, verticalalignment='bottom')
plt.text(0.5, -0.594, "(0.5, -0.594)", fontsize=9, verticalalignment='bottom')
plt.text(1.5, 0.394, "(1.5, 0.394)", fontsize=9, verticalalignment='bottom')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function and Tangent Line at x = -0.25")
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True)
plt.legend()

plt.show()