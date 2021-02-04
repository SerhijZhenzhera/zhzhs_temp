'''
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
Input: Iterable
Output: Iterable
Precondition: elements can be ints or strings
The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen 
'''

from collections import Counter


def frequency_sort(items):
    result = []
    result_temp = []
    temp = Counter(items)
    for it in items:
        t = (it, temp[it])
        if not t in result_temp:
            result_temp.append(t)

    def keyFunc(item):
        return item[1]

    result_temp.sort(key=keyFunc, reverse=True)

    for r in result_temp:
        for i in range(1, r[1]+1):
            result.append(r[0])
    return result


if __name__ == '__main__':

    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [
        4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
        'bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [
        4, 4, 4, 4, 2, 2, 2, 6, 6]
