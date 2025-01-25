
dict1 = {'Книга': [('Журавль и Лягушка', '120', '10')]}
dict2 = {'Книга': [('Золушка', '200', '40')]}
result = {}
for d in [dict1, dict2]:
    for key, value in d.items() :
        if key  not in result:
            result[key] = []
            result[key].extend(value)
            print(result)





