print(",".join(
    filter(lambda x: int(x, 2) % 5 == 0, input("Please enter comma separated numbers in binary:- ").split(','))))
