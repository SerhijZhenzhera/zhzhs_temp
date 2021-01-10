'''
Try to find out how many zeros a given number has at the end.
Input: A positive Int
Output: An Int. 
'''


def end_zeros(num: int) -> int:
    result = 0
    num_list = list(str(num))
    for i in range(len(num_list)):
        if num_list[len(num_list)-1] == '0':
            result += 1
            num_list.pop()
    print(num_list) # test
    print(result) # test
    return result


end_zeros(10100) # test
