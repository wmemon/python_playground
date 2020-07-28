"""
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.
"""


class Circle():
    def __init__(self, radius):
        self.radius = float(radius)

    def get_area(self):
        return float(3.14*self.radius ** 2)


c1 = Circle('wasim')
print(c1.get_area())
