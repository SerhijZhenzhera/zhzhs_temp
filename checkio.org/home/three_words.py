'''
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession.
Input: A string with words.
Output: The answer as a boolean.
How it is used: This teaches you how to work with strings and introduces some useful functions.
Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
0 < len(words) < 100 
'''


def checkio(words: str) -> bool:
    result = 0
    bool_result = None
    for word in words.split():
        if not word.isdigit():
            result += 1
            if result == 3:
                return True
        else:
            result = 0
    bool_result = True if result >= 3 else False
    return bool_result


if __name__ == '__main__':

    assert checkio("Hello World hello") == True
    assert checkio("He is 123 man") == False
    assert checkio("1 2 3 4") == False
    assert checkio("bla bla bla bla") == True
    assert checkio("Hi") == False
    assert checkio('one two 3 four five six 7') == True
