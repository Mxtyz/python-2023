pacientes = []

#Intruducir informacion del paciente
for i in range(4):
    print(f"Ingresando datos del paciente {i+1}:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    peso = float(input("Peso: "))
    sintomas = input("Síntomas (separados por comas): ").split(",")
    
    d_paciente = {
        "Nombre": nombre,
        "Edad": edad,
        "Peso": peso,
        "Sintomas": sintomas
    }
    
    pacientes.append(d_paciente)

# Búsquecar el paciente por su nombre
nombre_a_buscar = input("Ingrese el nombre del paciente que desea buscar: ")

buscar_p = False
for d_paciente in pacientes:
    if d_paciente["Nombre"] == nombre_a_buscar:
        print("\nFicha del paciente encontrado:")
        print("Nombre:", d_paciente["Nombre"])
        print("Edad:", d_paciente["Edad"])
        print("Peso:", d_paciente["Peso"])
        print("Síntomas:", d_paciente["Sintomas"])
        buscar_p = True
        break

if not buscar_p:
    print("No se encontró ningún paciente con ese nombre.")
