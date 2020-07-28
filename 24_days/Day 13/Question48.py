"""
Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.

"""


class Rectangle:
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def get_area(self):
        return self.width*self.length


r1 = Rectangle(2.5,3.6)
print(r1.get_area())