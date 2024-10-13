import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la onda
A = 0.06
k = 0.02 * np.pi
omega = 4 * np.pi

# 1. Gráfico de y vs. t en x = 0
t = np.linspace(0, 1, 1000)
y_t = -A * np.sin(omega * t)

plt.figure(figsize=(10, 5))
plt.plot(t, y_t, label='y(0, t)')
plt.title('Función de Onda vs. Tiempo en x = 0')
plt.xlabel('Tiempo (s)')
plt.ylabel('y (m)')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()

# 2. Gráfico de y vs. x en t = 0
x = np.linspace(0, 100, 1000)
y_x = A * np.sin(k * x)

plt.figure(figsize=(10, 5))
plt.plot(x, y_x, label='y(x, 0)')
plt.title('Función de Onda vs. Longitud del Medio en t = 0')
plt.xlabel('Longitud (m)')
plt.ylabel('y (m)')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
