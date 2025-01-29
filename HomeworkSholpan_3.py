guests = set()
while True:
    name = input()
    if name == "":
        break
    guests.add(name)
print(len(guests))

dict1 = {'Книга': [('Журавль и Лягушка', '120', '10')]}
dict2 = {'Книга': [('Золушка', '200', '40')]}

for key, value in dict2.items():
    if key in dict1:
        dict1[key].extend(value)
    else:
        dict1[key] = value
print(dict1)