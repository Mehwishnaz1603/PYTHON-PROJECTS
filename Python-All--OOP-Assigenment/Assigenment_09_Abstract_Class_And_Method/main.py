#--------Assigenment 09---------#
#Abstract Class And Methods:
#Use the abs module to create an abstract class shape with an abstract method area(). Inherit a Class Rectangle that
#implements arae.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

if __name__ == "__main__":
   rectangle = Rectangle(4, 7)
   print("Area of rectangle:", rectangle.area())
