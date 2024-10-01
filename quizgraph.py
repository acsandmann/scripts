import numpy as np
import matplotlib.pyplot as plt

def graph_1(x):
    return np.full_like(x, 6)

def graph_1_derivative(x):
    return np.zeros_like(x)


def graph_2(x):
    return -x + 2

def graph_2_derivative(x):
    return np.full_like(x, -1)

def graph_3(x):
    return np.log(x + 1)

def graph_3_derivative(x):
    return 1 / (x + 1)

def graph_4(x):
    return np.sin(x) * (x**2)

def graph_4_derivative(x):
    return 2 * x * np.sin(x) + x**2 * np.cos(x)


x = np.linspace(-5, 5, 400)
x_positive = np.linspace(0.1, 15, 400)

fig, axs = plt.subplots(4, 2, figsize=(10, 16))

# Graph 1
axs[0, 0].plot(x, graph_1(x), color='red')
axs[0, 0].set_title("Graph 1: Original Function")
axs[0, 1].plot(x, graph_1_derivative(x), color='blue')
axs[0, 1].set_title("Graph 1: Derivative")

# Graph 2
axs[1, 0].plot(x, graph_2(x), color='red')
axs[1, 0].set_title("Graph 2: Original Function")
axs[1, 1].plot(x, graph_2_derivative(x), color='blue')
axs[1, 1].set_title("Graph 2: Derivative")

# Graph 3
axs[2, 0].plot(x_positive, graph_3(x_positive), color='red')
axs[2, 0].set_title("Graph 3: Original Function")
axs[2, 1].plot(x_positive, graph_3_derivative(x_positive), color='blue')
axs[2, 1].set_title("Graph 3: Derivative")

# Graph 4
axs[3, 0].plot(x, graph_4(x), color='red')
axs[3, 0].set_title("Graph 4: Original Function")
axs[3, 1].plot(x, graph_4_derivative(x), color='blue')
axs[3, 1].set_title("Graph 4: Derivative")

plt.tight_layout()
plt.show()
