def decimal_a_binario(n):
    return bin(n)[2:]

def decimal_a_octal(n):
    return oct(n)[2:]

def decimal_a_hexadecimal(n):
    return hex(n)[2:]

# Ejemplo de uso
numero = int(input("Ingrese un número natural en formato decimal: "))

print(f"Binario: {decimal_a_binario(numero)}")

print(f"Octal: {decimal_a_octal(numero)}")

print(f"Hexadecimal: {decimal_a_hexadecimal(numero)}")