'''
In a given string you should reverse every word, but the words should stay in their places.
Input: A string.
Output: A string.
Precondition: The line consists only from alphabetical symbols and spaces.  
'''

def backward_string_by_word(text: str) -> str:    

    text_result = ''
    text = text.replace(' ', '@ @')
    text_list = text.split()
    for t in text_list:
        t = t[::-1]
        text_result += ' '
        text_result += t
    for i in range(len(text)-1):
        try:
            if text[i] == '@':
                text_result = text_result.replace('@', '')
        except:
            IndexError
    return text_result[1:]


if __name__ == '__main__':

    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
