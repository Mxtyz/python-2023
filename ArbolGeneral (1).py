import matplotlib.pyplot as plt
import numpy as np

# Definir los parámetros del problema
alpha = np.radians(30)  # Ángulo del plano inclinado en radianes (por ejemplo, 30 grados)
d = 1  # Distancia desplazada por m2

# Coordenadas del plano inclinado
x_inclinado = np.linspace(0, 2, 100)
y_inclinado = x_inclinado * np.tan(alpha)

# Coordenadas de m1 y m2
m1_x = 0
m1_y = 0
m2_x = 0
m2_y = d

# Crear la figura y el gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_inclinado, y_inclinado, label="Plano Inclinado")

# Marcar las posiciones de m1 y m2
plt.scatter(m1_x, m1_y, color='blue', label="m1 (origen)")
plt.scatter(m2_x, m2_y, color='red', label="m2")

# Dibujar la cuerda
plt.plot([m1_x, m2_x], [m1_y, m2_y], color='green', linestyle='--', label="Cuerda")

# Anotaciones
plt.text(m1_x, m1_y, "m1 (origen)", fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(m2_x, m2_y, "m2", fontsize=12, verticalalignment='bottom', horizontalalignment='right')

# Configuración del gráfico
plt.title("Sistema de Referencia para el Problema 2")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
