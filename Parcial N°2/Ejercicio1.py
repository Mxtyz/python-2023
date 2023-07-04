#Desarrolla una aplicación para gestionar una lista circular bidireccional de contactos telefónicos.
#Cada contacto tiene un nombre, un número de teléfono y una dirección de correo electrónico. Se
#debe implementar una lista circular bidireccional para almacenar los contactos. La lista debe
#tener las siguientes funcionalidades. Debe contener las siguientes funciones:
#A. Clases respectivas del problema
#B. Método para agregar un contacto a la lista
#C. Método para mostrar la lista de contactos
#D. Método para buscar un contacto por su nombre
#E. Método eliminar un contacto de la lista
#F. Método para verificar si la lista de contacto está vacía

#Nota: Se solicita no solo implementar las funciones requeridas, sino también probarlas y mostrar los
#resultados obtenidos anteriormente. Esto implica que se deben ejecutar las funciones con datos de
#prueba o ejemplos específicos para demostrar su funcionamiento.


#Se crea la clase contacto junto su funcion 
class Contacto:
    def __init__(self, nombre, telefono, correo):  
        self.nombre = nombre  
        self.telefono = telefono  
        self.correo = correo  
        self.siguiente = None  
        self.anterior = None  

#Se crea otra clase de nombre lista de contactos
class ListaContactos: 
 
#Se crean las demas funciones
    def __init__(self): 
        self.inicio = None 
#Se crea funcion 
    def esta_vacia(self):  
        return self.inicio is None 
    
#Se crea funcion para agregar los contactos 
    def agregar_contacto(self, nombre, telefono, correo): 
        nuevo_contacto = Contacto(nombre, telefono, correo)  

#Se implementa un if y else para los contactos 
        if self.esta_vacia(): 
            nuevo_contacto.siguiente = nuevo_contacto  
            nuevo_contacto.anterior = nuevo_contacto  
            self.inicio = nuevo_contacto  
        else:
            ultimo_contacto = self.inicio.anterior  
            nuevo_contacto.siguiente = self.inicio 
            nuevo_contacto.anterior = ultimo_contacto  
            self.inicio.anterior = nuevo_contacto  
            ultimo_contacto.siguiente = nuevo_contacto  
     
#Se crea una fucnion para eliminar contactos
    def eliminar_contacto(self, nombre):
        if self.esta_vacia():
            return
#Se crea una variable la cual es = a self.inicio
        contac = self.inicio

#Se crea un while true eliminar contactos
        while True:
            if contac.nombre == nombre:
                siguiente_contacto = contac.siguiente
                anterior_contacto = contac.anterior
                anterior_contacto.siguiente = siguiente_contacto
                siguiente_contacto.anterior = anterior_contacto

                if contac == self.inicio: 
                    self.inicio = siguiente_contacto 

                del contac   
                break 

            contac = contac.siguiente 
            if contac == self.inicio: 
                break 

#Se imprimen en pantalla los contactos  
    def mostrar_contactos(self): 
        if self.esta_vacia(): 
            print("La lista de contactos está vacía.")
        else:
            contac = self.inicio  

            while True:
                print("Nombre: ", contac.nombre) 
                print("Teléfono: ", contac.telefono) 
                print("Correo: ", contac.correo) 

                contac = contac.siguiente 
                if contac == self.inicio: 
                    break 

#El codigo se ejecuta pero no logro hacer que imprima en pantalla los nombres, telefonos o correo.