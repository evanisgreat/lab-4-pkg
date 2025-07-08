from abc import ABC, abstractmethod
import math 


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Square(Shape):
    def __init__(self, side: float):
    # store side length
        self.side = side

    
    def area(self) -> float:
    # return side**2
        return self.side ** 2
    

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius**2