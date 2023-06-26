#Crear clase Empleado
class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinados = []

# Se crean las demas funciones 
    def agregarsubordinado(self, subordinado): 
        self.subordinados.append(subordinado) 

    def eliminarsubordinado(self, subordinado): 
        self.subordinados.remove(subordinado) 
 
    def obtenerjerarquia(self, nivel=0): 
        indentacion = "    " * nivel
        print(f"{indentacion}- {self.nombre} ({self.cargo})")
        for subordinado in self.subordinados:
            subordinado.obtenerjerarquia(nivel + 1)

    def buscarempleado(self, nombre): 
        if self.nombre.lower() == nombre.lower(): 
            print(f"Cargo: {self.cargo}")
            if len(self.subordinados) > 0: 
                print("Subordinados:")
                for subordinado in self.subordinados:
                    print(f"- {subordinado.nombre} ({subordinado.cargo})")
        else:
            for subordinado in self.subordinados:
                subordinado.buscarempleado(nombre)

    def obtenerjefedirecto(self, empleado): 
        for subordinado in self.subordinados:
            if subordinado.nombre.lower() == empleado.nombre.lower():
                print(f"Jefe directo de {empleado.nombre}: {self.nombre} ({self.cargo})")
                return
            else:
                subordinado.obtenerjefedirecto(empleado)

directivo1 = Empleado("Directivo1", "Cargo1")  

# Agregar empleados
directivo2 = Empleado("Directivo2", "Cargo2")  
directivo1.agregarsubordinado(directivo2)
directivo3 = Empleado("Directivo3", "Cargo3")  
directivo1.agregarsubordinado(directivo3)
gerente1 = Empleado("Gerente1", "Gerente") 
directivo2.agregarsubordinado(gerente1)
gerente2 = Empleado("Gerente2", "Gerente")  
directivo3.agregarsubordinado(gerente2) 
empleado1 = Empleado("Empleado1", "Empleado")
gerente1.agregarsubordinado(empleado1) 

# Mostrar jerarquía
print("Jerarquía completa de la empresa:")
directivo1.obtenerjerarquia()

# Buscar empleado 
print("\nBuscar empleado:") 
directivo1.buscarempleado("Gerente1") 
 
# Obtener jefe directo
print("\nObtener jefe directo:") 
gerente1.obtenerjefedirecto(empleado1) 
  