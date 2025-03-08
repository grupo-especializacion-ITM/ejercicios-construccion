class Empleado:
    def __init__(self, nombre):
        self.nombre     = nombre

class Funciones:
    def getFunctions(self,nombre):
        print(f"se consultan las funciones del empleado {nombre}")
        return ["funcion1", "funcion2"]
    
class Sueldo:
    def getSalary(self,nombre):
        print(f"se consulta en base de datos el sueldo del empleado {nombre}")
        return 1000
    
empleado  = Empleado("Juan")
funciones = Funciones().getFunctions(empleado.nombre)
sueldo    = Sueldo().getSalary(empleado.nombre)