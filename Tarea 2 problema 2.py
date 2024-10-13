import numpy as np
import matplotlib.pyplot as plt

# Definir las constantes
m = 0.2  # kg
k = 5  # N/m
b = 1.5  # Ns/m
F0 = 10  # N

# Calcular la frecuencia natural
omega0 = np.sqrt(k / m)

# Calcular la frecuencia de resonancia
omega_r = np.sqrt(omega0**2 - (b**2) / (4 * m**2))

# Calcular la amplitud y fase para omega = 2*omega_r
X = F0 / np.sqrt((5 - (2 * omega_r)**2)**2 + (2 * 1.5 * 2 * omega_r)**2)
delta = np.arctan2(2 * 1.5 * 2 * omega_r, 5 - (2 * omega_r)**2)

# Definir la función de posición para omega = 2*omega_r
def x(t):
    return X * np.cos(2 * omega_r * t - delta)

# Crear datos de tiempo
t = np.linspace(0, 2 * np.pi / (2 * omega_r), 1000)

# Crear datos de posición
x_values = x(t)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(t, x_values, label=r'$\omega = 2\omega_r$', color='blue')
plt.title('Posición vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.grid(True)
plt.legend()
plt.show()