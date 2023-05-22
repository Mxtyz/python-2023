import numpy as np
m = np.random.randint(0, 10, size=(3, 3))
print("la matriz es:",m)
A = np.linalg.inv(m)
print("La matriz inversa es:",A)

identidad = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(identidad)

iden = m * A
print("La Matriz identidad es:",iden)
