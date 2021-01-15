'''
You have a number and you need to determine which digit in this number is the biggest.
Input: A positive int.
Output: An Int (0-9). 
'''

def max_digit(number: int) -> int:
    list_digit = list(str(number))
    return int(max(list_digit))
