import random

#Crear clase Cliente 
class Cliente:
    def __init__(self, ticket, caja):
        self.ticket = ticket
        self.caja = caja

# Crear clase colaAtender 
class ColaAtencion:
    def __init__(self):
        self.cola = []
        self.caja_actual = 0

    def agregarcliente(self, cliente):
        self.cola.append(cliente)

    def atendercliente(self):
        if len(self.cola) > 0:
            cliente = self.cola.pop(0)
            self.caja_actual = (self.caja_actual + 1) % 3
            print(f"Atendiendo cliente {cliente.ticket} en Caja {cliente.caja}")
        else:
            print("No hay clientes en la cola.")

    def mostrarcola(self):
        if len(self.cola) > 0:
            print("Cola de atención:")
            for cliente in self.cola:
                print(f"Ticket: {cliente.ticket}, Caja: {cliente.caja}")
        else:
            print("No hay clientes en la cola.")

cola = ColaAtencion()
# Agregar clientes a la cola
cola.agregarcliente(Cliente(random.randint(1, 100), random.randint(1, 3)))
cola.agregarcliente(Cliente(random.randint(1, 100), random.randint(1, 3)))
cola.agregarcliente(Cliente(random.randint(1, 100), random.randint(1, 3)))
cola.agregarcliente(Cliente(random.randint(1, 100), random.randint(1, 3)))
cola.agregarcliente(Cliente(random.randint(1, 100), random.randint(1, 3)))

# Mostrar la cola
cola.mostrarcola()

cola.atendercliente()
cola.atendercliente()
cola.atendercliente()

# Mostrar la cola después de atender algunos clientes
cola.mostrarcola()
