import numpy as np
import matplotlib.pyplot as plt

# 1. Graph of total number of people who have tried a product (S-shaped logistic growth)

# Logistic function to simulate product adoption
def logistic_growth(t, L=100, k=0.3, x0=10):
    return L / (1 + np.exp(-k * (t - x0)))

t = np.linspace(0, 30, 300)
population = logistic_growth(t)

plt.figure(figsize=(8, 6))
plt.plot(t, population, label='Total number of people who tried the product', color='blue')
plt.title('Product Adoption Over Time')
plt.xlabel('Time')
plt.ylabel('Total People')
plt.grid(True)
plt.legend()
plt.show()

# 2. Cost Function (Linear graph of cost function C(q) = 5000 + 4q)

q = np.array([0, 5, 10, 15, 20])
C_q = 5000 + 4 * q

plt.figure(figsize=(8, 6))
plt.plot(q, C_q, marker='o', color='green', label='Cost Function C(q) = 5000 + 4q')
plt.title('Cost Function vs Quantity')
plt.xlabel('Quantity (q)')
plt.ylabel('Cost ($)')
plt.grid(True)
plt.legend()
plt.show()

# 3. Exponential Growth Function P = 5(1.07)^t

t_exp = np.linspace(0, 30, 300)
P_t = 5 * (1.07 ** t_exp)

plt.figure(figsize=(8, 6))
plt.plot(t_exp, P_t, color='orange', label='Exponential Growth: P(t) = 5(1.07)^t')
plt.title('Exponential Growth Function')
plt.xlabel('Time (t)')
plt.ylabel('P(t)')
plt.grid(True)
plt.legend()
plt.show()

# 5. World population growth (P(t) = 7.17 * (1.011)^t)

t_world = np.linspace(0, 100, 300)  # Years since 2014
P_world = 7.17 * (1.011 ** t_world)

plt.figure(figsize=(8, 6))
plt.plot(t_world, P_world, color='red', label='World Population Growth')
plt.title('World Population Growth (2014 onwards)')
plt.xlabel('Years since 2014')
plt.ylabel('Population (in billions)')
plt.grid(True)
plt.legend()
plt.show()