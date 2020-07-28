def square(num):

    """
    This function takes a number to return square of it.
    :param num: float or int
    :return: float
    """
    if not (isinstance(num,int) or isinstance(num,float)):
        return "Only integers and floats accepted as parametres."
    if not num:
        return "Please enter a number."
    return num**2



def main():
    print(square.__doc__)

if __name__ == '__main__':
    main()

