import matplotlib.pyplot as plt
import numpy as np

def derivative(x):
    return np.piecewise(x,
                        [x < -2, (-2 <= x) & (x < 0), (0 <= x) & (x < 1), (1 <= x) & (x < 2), x >= 2],
                        [lambda x: -1,   
                         lambda x: 1,    
                         lambda x: -0.5, 
                         lambda x: 0.5,  
                         lambda x: -1.5])

x_vals = np.linspace(-3, 3, 400)

plt.plot(x_vals, derivative(x_vals), label="f'(x)", color='blue')

critical_points = [-2, 0, 1, 2]
plt.scatter(critical_points, [0, 0, 0, 0], color="red", zorder=5)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)

plt.xlabel("x")
plt.ylabel("f'(x)")
plt.title("Derivative of the Given Function")
plt.grid(True)
plt.legend()

plt.show()