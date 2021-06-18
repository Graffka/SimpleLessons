from abc import ABC, abstractmethod, abstractproperty


class Movable(ABC):
    #__metaclass__ = ABCMeta

    @abstractmethod
    def move(self):
        pass

        """Переместить объект"""

    @abstractmethod
    def speed(self):
        pass
        """Скорость объекта"""


class Car(Movable):
    def __init__(self):
        self.speed = 10
        self.x = 0

    def move(self):
        self.x += self.speed

    def speed(self):
            return self.speed


class Truck(Movable):
    def __init__(self):
        self.speed = 5
        self.x = 1

    def move(self):
        self.x += self.speed

    def speed(self):
            return self.speed




Audi = Car()
Volvo = Truck()
Audi.x