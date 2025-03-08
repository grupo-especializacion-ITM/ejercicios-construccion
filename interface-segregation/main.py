from abc import ABC, abstractmethod

# Interfaz solo para trabajar
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

# Interfaz solo para comer
class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

# Humano implementa ambas interfaces
class Human(Workable, Eatable):
    def work(self):
        print("Human is working.")

    def eat(self):
        print("Human is eating.")

# Robot solo implementa Workable, sin verse obligado a implementar eat()
class Robot(Workable):
    def work(self):
        print("Robot is working.")

# Uso del sistema
human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()  # No hay métodos innecesarios en la clase Robot
