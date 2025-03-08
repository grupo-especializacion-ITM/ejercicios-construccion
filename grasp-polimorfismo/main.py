from abc import ABC, abstractmethod
import math

# Clase base abstracta (interfaz) que define el comportamiento común
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        """Método abstracto que todas las figuras deben implementar"""
        pass

# Subclase concreta: Círculo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2

# Subclase concreta: Rectángulo
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto

# Función que usa polimorfismo para calcular el área sin importar el tipo de figura
def imprimir_area(figura: Figura):
    print(f"El área es: {figura.calcular_area():.2f}")

# Ejemplo de uso
circulo = Circulo(radio=5)
rectangulo = Rectangulo(ancho=4, alto=6)

imprimir_area(circulo)      # Salida: El área es: 78.54
imprimir_area(rectangulo)   # Salida: El área es: 24.00