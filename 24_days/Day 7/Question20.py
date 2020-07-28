"""
Define a class with a generator which can iterate the numbers,
 which are divisible by 7, between a given range 0 and n.
"""

class div_by_seven:
    def __init__(self,stop):
        self.stop = stop

    def special_for(self,n=0):
        n = self.stop
        iterator = iter(range(n+1))
        while True:
            try:
                num = next(iterator)
                if num%7 == 0:
                    print(num)
            except StopIteration:
                break
        return None

o1 = div_by_seven(63)
o1.special_for()