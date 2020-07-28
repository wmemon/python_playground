"""
Define a custom exception class which takes a string message as attribute.
"""

class CustomException(Exception):
    def __init__(self,message):
        self.message = message

raise CustomException("This is a custom error. ")