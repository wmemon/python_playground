principal = 10000
n = 12
r = 8
t = int(input("Please enter the time period:- "))
print(f"The amount after {t} years is {(principal)*((1+((r/100)/n))**(n*t))}")
