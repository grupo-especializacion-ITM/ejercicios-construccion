class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def getSalary(self):
        print(f"se consulta en base de datos el sueldo del empleado {self.nombre}")
        return 1000
    
    def getFunctions(self):
        print("se consultan las funciones del empleado")
        return ["funcion1", "funcion2"]
    
empleado = Empleado("Juan")
print(empleado.getSalary())
print(empleado.getFunctions())