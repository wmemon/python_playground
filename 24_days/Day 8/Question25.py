"""
Define a class, which have a class parameter and have a same instance parameter.
"""

class same:
    def __init__(self,param1=None):
        self.param1 = param1


s1 = same()
s1.param1 = 'wasim'
print(s1.param1)