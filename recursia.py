def sum_nested_list(lst):
    tal = 0
    for element in lst:
        if isinstance(element, list):
            tal += sum_nested_list(element)
        else:
            tal += element
    return tal


nested_list = [1, [2, 3, [4, 5]], 6, [7, [8, 9]], 10]
result = sum_nested_list(nested_list)
print(result)
