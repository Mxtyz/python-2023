import numpy as np
import matplotlib.pyplot as plt

# Datos del Problema 1
m = 0.5  # masa en kg
k = 78.96  # constante de restauración en N/m
A = 0.1  # amplitud en m
omega = np.sqrt(k / m)  # frecuencia angular en rad/s
T = 2 * np.pi / omega  # periodo en s

# Tiempo para graficar (un periodo completo)
t = np.linspace(0, T, 500)
y = A * np.cos(omega * t)

# Graficar Altura vs. Tiempo para Movimiento Armónico Simple
plt.figure(figsize=(10, 6))
plt.plot(t, y, label=f'$y(t) = 0.1 \\cos({omega:.2f} t)$')
plt.title('Altura vs. Tiempo para Movimiento Armónico Simple')
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura (m)')
plt.legend()
plt.grid(True)
plt.show()
