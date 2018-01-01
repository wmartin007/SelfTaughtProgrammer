""" Define a class called Apple with 4 instance variables that represent
four attributes of an apple"""
from math import pi


class Apple():
    def __init(self, color, size, texture, acidity):
        self.color = color
        self.size = size
        self.texture = texture
        self.acidity = acidity

"""Create a circle clas with method called area that calcs and retuns the area.
Then create a circle object and call area on it"""
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius**2) * pi

cir = Circle(10)
print(cir.area())

"""Create a Triangle class with method called area that calcs and returns the
area. Then create a Triangle object and call area on it
"""

class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

tri = Triangle(25, 30)
print(tri.area())


"""Make a Hexagon class with a method called calculate permiter. Then create
a Hexagon object, call calculate_perimiter and print the result"""

class Hexagon():
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return self.side_length * 6


hex = Hexagon(4)
print(hex.calculate_perimeter())
