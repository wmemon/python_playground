"""

    Assuming that we have some email addresses in the "username@companyname.com" format,
    please write program to print the user name of a given email address.
    Both user names and company names are composed of letters only.
    Example: If the following email address is given as input to the program:

Input: john@google.com
Output: john

"""

def get_username(email):
    """
    This function takes an email string as an input and returns a string username as output
    :param email: str
    :return: None | str
    """
    if not isinstance(email,str):
        return None

    return(email.split('@')[0])

print(get_username('wmemon579@gmail.com'))
print(get_username('john@google.com'))

