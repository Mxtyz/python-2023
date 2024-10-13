import numpy as np
import matplotlib.pyplot as plt

# Definir la función de posición angular
def theta(t):
    return (np.pi/16) * np.exp(-t/48) * np.sin(2.21 * t)

# Crear datos de tiempo
t = np.linspace(0, 10, 1000)

# Crear datos de posición angular
theta_values = theta(t)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(t, theta_values, label=r'$\theta(t) = \frac{\pi}{16} e^{-\frac{t}{48}} \sin(2.21t)$', color='blue')
plt.title('Posición Angular vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición Angular (rad)')
plt.grid(True)
plt.legend()
plt.show()

# Definir la función de posición angular para el caso sobreamortiguado
def theta_overdamped(t):
    return (np.pi/16) * (np.exp(-t/24) + np.exp(-t/24))

# Crear datos de posición angular para el caso sobreamortiguado
theta_overdamped_values = theta_overdamped(t)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(t, theta_overdamped_values, label=r'$\theta(t) = \frac{\pi}{16} (e^{-\frac{t}{24}} + e^{-\frac{t}{24}})$', color='red')
plt.title('Posición Angular vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición Angular (rad)')
plt.grid(True)
plt.legend()
plt.show()