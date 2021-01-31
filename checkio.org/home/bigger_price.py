'''
You have a table with all available goods in the store. The data is represented as a list of dicts
Your mission here is to find the TOP most expensive goods.
The amount we are looking for will be given as a first argument and the whole data as the second one
Input: int and list of dicts. Each dicts has two keys "name" and "price"
Output: the same as the second Input argument.  
'''

def bigger_price(limit: int, data: list) -> list:
    temp_list = []
    result_list = []
    for dt in data:
        temp_list.append(dt.get("price"))
    temp_list.sort(reverse=True)
    data_list = temp_list[:limit]
    for num in data_list:
        for dt in data:
            if num in dt.values():
                result_list.append(dt)
    return result_list


if __name__ == '__main__':
    
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ]

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}]
