'''
You have a string that consist only of digits.
You need to find how many zero digits ("0") are at the beginning of the given string.
Input: A string, that consist of digits.
Output: An Int.
Precondition: 0-9  
'''


def beginning_zeros(number: str) -> int:
    result = 0
    for el in list(number):
        if el == '0':
            result += 1
        else:
            break
    return result
