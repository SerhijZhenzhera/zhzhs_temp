'''
Not all of the elements are important.
What you need to do here is to remove from the list all of the elements before the given one.
Input: List and the border element.
Output: Iterable (tuple, list, iterator ...). 
'''


def remove_all_before(items: list, border: int):
    for item in items:
        if int(item) == border:
            ind = items.index(item)          
            items = items[ind:]
            return items
        else:
            pass
    return items    
