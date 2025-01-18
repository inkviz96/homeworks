# task 1
# В ночном клубе фиксируется список гостей.
# Причем гости могут выходить из помещения, а затем, снова заходить.
# Тогда их имена фиксируются повторно. На вход программы поступает такой список
# (каждое имя записано с новой строки).
# Например:
# Сергей
# Мария
# Наталья
# Евгений
# Сергей
# Мария
# …
# пока не будет введена пустая строка.
# Требуется подсчитать общее число гостей, которые посетили ночной клуб.
# Полагается, что гости имеют уникальные имена.
# На экран вывести общее число гостей клуба.

def counter_visitors(*args):
    return len(set(args))   # Возвращаем длину множества с уникальными именами
print(counter_visitors("Сергей", "Мария", "Наталья", "Евгений", "Сергей", "Мария"))

# # or

def counter_visitors():
    visitors = set()  # Создаем множество куда запишутся уникальные имена
    while True:       # Старт цикла
        name = input("Enter name of visitor: ")
        if name == "":   # Условие остановки цикла при вводе пустой строки
            break
        visitors.add(name)    # Добавляем имена посетителей во множество
    print(f"Total number of visitors: {len(visitors)}" ) # Печатаем кол-во посетителей

counter_visitors() # Вызываем функцию


# task 2
# Надо объединить значения в словаре под одним одинаковым ключом
# К примеру:
# {'Книга': [('Журавль и Лягушка', '120', '10')]}
# {'Книга': [('Золушка', '200', '40')]}
# При выполнении кода должно получится:
# {'Книга': [('Журавль и Лягушка', '120', '10'), ('Золушка', '200', '40')]}

dict1 = {'Книга': [('Журавль и Лягушка', '120', '10')]}
dict2 = {'Книга': [('Золушка', '200', '40')]}
for key in dict1:
    if key in dict2:
        dict1[key].append(*dict2[key])
print(dict1)

# or

dict1 = {'Книга': [('Журавль и Лягушка', '120', '10')]}
dict2 = {'Книга': [('Золушка', '200', '40')]}
dict3 = {}

def merging_dictionaries(dict1, dict2):
    for key in dict1:    # Старт цикла
        if key in dict2:  # Условие совпадения ключей из dict1 в dict2
            dict3[key] = [*dict1[key],*dict2[key]]   # Распаковка и добавление значений
    return dict3
result = merging_dictionaries(dict1, dict2)   # Вызываем функцию
print(result)






