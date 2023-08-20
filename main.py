class Asiento:
     #Con el inicializador creo los atributos de instancia
     def __init__(self,color,precio,registro):
         self.color = color
         self.precio = precio
         self.registro = registro

     #Los metodos de instancia llevan siempre como primer parametro la palabra self
     def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
             #luego de verificar que este entre los permitidos
             #el atributo color del objeto tendra el valor de color 
             self.color = color

class Auto:
     #Atributo de clase
     cantidadCreados = 0
     
     #Inicializador, atributos de instancia
     def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        #Si bien el diagrama UML indica que el atributo de asientos es un array
        #Como python no es fuertemente tipado, no debemos indicar que asientos es un array
        self.asientos = asientos
        self.marca = marca
        #Al atributo motor, estamos asignando un objeto de la clase Motor
        self.motor = motor
        self.registro = registro

     def cantidadAsientos(self):
        cantidad = 0
        #Si bien, no indicamos que asientos sea un array
        #el in significa tambien recorrer los caracteres que conforman una palabra, por eso no bota error
        for elemento in self.asientos:
            #Usando la función type
            #Comprobamos que cada elemento del atributo asientos, sea el tipo de dato Asientos(quien es una clase) 
            if type(elemento) == Asiento:
                cantidad += 1
        return (cantidad)
     
     def verificarIntegridad(self):
        #Los metodos de instancia los usan instancias/objetos, por eso siempre llevan el self
        #Ese self, se reemplaza por el objeto que esta llamando al metodo
        #nombre_del_objeto.nombre_del_atributo
        #Como el atributo motor es tambien un objeto, escribimos el atributo que queremos acceder
        if self.registro == self.motor.registro:
            for elemento in self.asientos:
                if elemento.registro != self.registro:
                    return("Las piezas no son originales")
                else:
                    return("Auto original")
        #Como el if no fue verdad, entonces retorne el siguiente texto
        return("Las piezas no son originales")

class Motor:
     def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
     
     def cambiarRegistro(self,registro):
         self.registro = registro

     def asignarTipo(self,tipo):
         if tipo == "electrico" or tipo == "gasolina":
             self.tipo = tipo

     
        