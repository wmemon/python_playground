import re
import getpass
def password_checker(password):
    pattern = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$]).{6,12}$")
    a = pattern.search(password)
    if a:
        return password
    return False

def main():
    print(','.join(filter(password_checker,input("Enter password in csv format:- ").split(','))))

if __name__ == '__main__':
    main()