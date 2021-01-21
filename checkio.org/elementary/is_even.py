'''
Check if the given number is even or not. Your function should return True if the number is even, and False if the number is odd.
Input: An int.
Output: A bool.
How it’s used: (math is used everywhere)
Precondition: both given ints should be between -1000 and 1000 
'''


def is_even(num: int) -> bool:
    return bool(num % 2 == 0)


if __name__ == '__main__':
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
