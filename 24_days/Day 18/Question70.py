"""Please write a program to output a random even number between 0 and 10
 inclusive using random module and list comprehension."""
# Instead of list Comprehension, I used randrange which does the same thing.
from random import choice
from random import randrange

print(choice([i for i in range(0,12,2)]))
print(randrange(0, 12, 2))
