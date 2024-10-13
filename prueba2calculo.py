import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear figura y ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear los límites del dominio
x = np.linspace(-10, 4, 100)  # x va desde -10 hasta 4
y = np.linspace(-3, 3, 100)   # y va desde -3 hasta 3
z = np.linspace(-1, 1, 100)   # z va desde -1 hasta 1

# Crear una malla para representar los límites en 3D
X, Y = np.meshgrid(x, y)
Y2, Z = np.meshgrid(y, z)
X2, Z2 = np.meshgrid(x, z)

# Graficar las superficies
# Límite x = 4 (superficie vertical)
ax.plot_surface(4 * np.ones_like(Y), Y, Z2, color='red', alpha=0.5)

# Límites y = -3 y y = 3 (superficies verticales)
ax.plot_surface(X, -3 * np.ones_like(X), Z2, color='green', alpha=0.5)
ax.plot_surface(X, 3 * np.ones_like(X), Z2, color='green', alpha=0.5)

# Límites z = -1 y z = 1 (superficies horizontales)
ax.plot_surface(X2, Y2, -1 * np.ones_like(X2), color='blue', alpha=0.5)
ax.plot_surface(X2, Y2, 1 * np.ones_like(X2), color='blue', alpha=0.5)

# Configurar los ejes
ax.set_xlim(-10, 4)
ax.set_ylim(-3, 3)
ax.set_zlim(-1, 1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar el gráfico
plt.show()
