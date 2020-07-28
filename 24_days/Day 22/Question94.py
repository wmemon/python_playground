"""
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
"""

def count_chicken_rabbit(heads, legs):
    heads = int(heads)
    legs = int(legs)
    if legs%2!=0:
        return "No Solution"
    else:
        rabbits = (legs-(2*heads))//2
        chickens = ((4*heads)-legs)//2
        return f"Chicken: {chickens} and Rabbits: {rabbits}."

print(count_chicken_rabbit(35,94))

