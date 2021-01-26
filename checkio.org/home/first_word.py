'''
You are given a string where you have to find its first word.
When solving a task pay attention to the following points:
    There can be dots and commas in a string.
    A string can start with a letter or, for example, a dot or space.
    A word can contain an apostrophe and it's a part of a word.
    The whole text can be represented with one word and that's it.
Input: A string.
Output: A string. 
How it is used: the first word is a command in a command line
Precondition: the text can contain a-z A-Z , . ' 
'''


def first_word(text: str) -> str:
    text += ' '
    for i in range(len(text)):
        if bool(text[i:i+1].isalpha()) == True or text[i:i+1] == "'":
            a = i
            break
        else:
            i += 1
    i = a
    for i in range(a, len(text)):
        if bool(text[i:i+1].isalpha()) == False and text[i:i+1] != "'":
            b = i
            c = text[a: b]
            break
        else:
            i += 1
    return c


if __name__ == '__main__':

    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
