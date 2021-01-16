'''
In a given list the first element should become the last one.
An empty list or list with only one element should stay the same. 
Input: List.
Output: Iterable. 
'''

# агрессивное решение без условной конструкции
def replace_first(items: list) -> Iterable:
    items.append('replace_first_mission') # для items = []
    rem_item = items.pop(0)
    items.append(rem_item)
    items.remove('replace_first_mission')
    return items


# безопасное решение
def replace_first(items): # return items.append(items.pop(0)) if items else items
    if not items == []:
        rem_item = items.pop(0)
        items.append(rem_item)
    else:
        pass
    return items
    