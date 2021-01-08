'''
In this mission, you need to create a password verification function.
The verification condition is: the length should be bigger than 6.
Input: A string.
Output: A bool.
'''


def is_acceptable_password(password):
    if type(password) is str:
        if len(password) > 6:
            return True
        else:
            print('At least 7 characters')
            return False
    else:
        ValueError
