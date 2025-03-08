from abc import ABC, abstractmethod

# Interfaz con demasiadas responsabilidades
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

# Humano implementa los métodos correctamente
class Human(Worker):
    def work(self):
        print("Human is working.")

    def eat(self):
        print("Human is eating.")

# Robot no necesita el método eat(), pero se ve obligado a implementarlo
class Robot(Worker):
    def work(self):
        print("Robot is working.")

    def eat(self):
        raise NotImplementedError("Robots don't eat!")  # Error innecesario

# Uso del sistema
human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
# robot.eat()  # Esto generaría un error innecesario