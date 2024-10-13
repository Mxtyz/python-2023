def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    return (a * b) // mcd(a, b)

def bezout(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return s0, t0

# Ejemplo de uso
a = int(input("Ingrese el primer número natural (a): "))
b = int(input("Ingrese el segundo número natural (b): "))

#MCD= Minimo comun divisor
#MCM= Maximo comun multiplo
#Coeficiente de Bezout

mcd_value = mcd(a, b)
mcm_value = mcm(a, b)
s, t = bezout(a, b)

print(f"MCD({a}, {b}) = {mcd_value}")
print(f"MCM({a}, {b}) = {mcm_value}")
print(f"Coeficientes de Bézout: s = {s}, t = {t}")
