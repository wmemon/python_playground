credits = int(input("Enter the number of credits earned:- "))


if credits>90:
    print("Senior status")

elif credits>60:
    print("Junior status")

elif credits>30:
    print("Sophomore Status")

else:
    print("Freshman Status")