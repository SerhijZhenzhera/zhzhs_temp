'''
You are given a string and you have to find its first word
-The input string consists of only English letters and spaces
-There aren’t any spaces at the beginning and the end of the string

'''


def first_word(a):
    if type(a) is str:
        a = a + ' '
        for i in range(len(a)):
            if not a[i:i+1] == ' ':
                i += 1
            else:
                b = a[:i]
                print(b) # test
                return b      
    else:
        ValueError
        print('Only text!')
