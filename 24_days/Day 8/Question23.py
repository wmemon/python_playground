def square(num):
    if not (isinstance(num,int) or isinstance(num,float)):
        return "Only integers and floats accepted as parametres."

    return num**2


print(square(float(input("Please enter the number (only float or int) accepted:- "))))