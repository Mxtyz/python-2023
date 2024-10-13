def secuencia_collatz(n):
    secuencia = []
    while n != 1:
        secuencia.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    secuencia.append(1)  # Agregar el 1 al final
    return secuencia

# Ejemplo de uso
numero = int(input("Ingrese un número natural: "))
resultado = secuencia_collatz(numero)

print("Secuencia de Collatz:")
print(" ".join(map(str, resultado)))  # Salida horizontal
# Para salida vertical, puedes usar:
# for num in resultado:
#     print(num)