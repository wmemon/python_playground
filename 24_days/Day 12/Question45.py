"""
Define a class named American which has a static method called printNationality.
"""

class American:
    pass

    @staticmethod
    def printNationality(nationality):
        print(nationality)

# A static method does not need an instance to work.
American.printNationality("Indian")