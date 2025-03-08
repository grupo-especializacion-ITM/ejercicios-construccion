from abc import ABC, abstractmethod
import math

class Figura:
    @abstractmethod
    def calcular_area(self):
        pass

# Clase concreta para Círculo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2

# Clase concreta para Rectángulo
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto

# Nueva clase CalculadoraArea que usa polimorfismo
class CalculadoraArea:
    def calcular(self, figura: Figura):
        if not isinstance(figura, Figura):
            raise ValueError("El argumento debe ser una instancia de Figura")
        return figura.calcular_area()
    
calc = CalculadoraArea()

# Creamos figuras
circulo = Circulo(radio=5)
rectangulo = Rectangulo(ancho=4, alto=6)

# Calculamos áreas
print(f"Área del círculo: {calc.calcular(circulo)}")  # Usa math.pi
print(f"Área del rectángulo: {calc.calcular(rectangulo)}")  # 24