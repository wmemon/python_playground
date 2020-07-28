"""
Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as following:

Input:- D 300
        D 300
        W 200
        D 100
Output:- 500
"""


# 1st idea is to use a class but we have only one user, so a function will work.

def calculate_money(inp_string):
    if not isinstance(inp_string, str):
        return "[!]Please follow the guidelines given."
    elif not (inp_string[0].upper() == 'D' or inp_string[0].upper() == 'W'):
        return "[!]Please follow the guidelines given."
    inp_string_li = inp_string.split(' ')
    if not len(inp_string_li) == 2:
        return "[!]Please follow the guidelines given."

    else:
        return [inp_string_li[0], int(inp_string_li[1])]


def main():
    money = 0
    print("Starting the program... ")
    print("Enter stop to stop")
    print("Enter D (money) to enter amount to deposit.")
    print("Enter W (money) to withdraw money.")
    while True:
        inp_string = input("Enter argument: ")
        if inp_string == 'stop':
            break
        if calculate_money(inp_string) == "[!]Please follow the guidelines given.":
            print("[!]Please follow the guidelines given.")

        elif calculate_money(inp_string)[0].upper() == 'D':
            money += calculate_money(inp_string)[-1]

        elif calculate_money(inp_string)[0].upper() == 'W':
            money -= calculate_money(inp_string)[-1]

    print(f"The final money count is : {money}")


if __name__ == '__main__':
    main()
