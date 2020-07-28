"""
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""

class Shape:
    def get_area(self,length=0.0):
        return length*length

class Square(Shape):
    def __init__(self,length = 0):
        self.length = float(length)

    def get_area(self):
        return self.length*self.length

s1 = Shape()
print(s1.get_area(5.5))
sq1 = Square(5.5)
print(s1.get_area(sq1.length))
print(sq1.get_area())
