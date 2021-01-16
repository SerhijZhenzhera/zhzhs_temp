'''
Split the string into pairs of two characters. If the string contains an odd number of characters,
then the missing second character of the final pair should be replaced with an underscore ('_').
Input: A string.
Output: An iterable of strings.
Precondition: 0<=len(str)<=100  
'''





def split_pairs(a):
    b = []
    if not len(a)%2 == 0: a += '_'
    for i in range(0, len(a)-1, 2):
        b.append(''.join([a[i], a[i+1]]))
    print(b)    
        

    
    
    
    # print([a[: len(a)//2], a[len(a)//2:]])
    # return [a[: len(a)//2], a[len(a)//2:]]
    
    
    

    

    
    
    

split_pairs('abcd')
split_pairs('abc')
