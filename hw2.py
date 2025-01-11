# 1 уровень сложности:
# Дан список:
# tst = [1, 2, 3, 4, 5]
# Прибавьте к его каждому элементу число 2 и выведите результат в консоль.


# tst = [1, 2, 3, 4, 5]
# for i in tst:
#     print(i + 2, end=' ')

# tst = [1, 2, 3, 4, 5]
# print(' '.join(str(i + 2) for i in tst))


# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
# Напишите с помощью тернарного оператора.

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
#
# for i in range(int(a), int(b) + 1):
#     print(i, end=' ')
#     if int(a) >= int(b):
#         print("First number must be less  than second")
# Не могу напечатать "First number must be less than second"


# print(" ".join(str(i) for i in range(a, b + 1)) if a <= b else print("First number must be greater than"))


# Дан список:
# tst = [1, 2, 3, 4, 5]
# Найдите сумму квадратов элементов этого списка.
# tst = [1, 2, 3, 4, 5]
# print(sum(i**2 for i in tst))


# Дано число:
# tst = 1234567
# Запишите из него в новый список только нечетные элементы.

# tst = 1234567
# new_tst = []

# for i in str(tst):
#     if int(i) % 2 != 0:
#         new_tst.append(int(i))
#
# print(new_tst)

# print([int(i) for i in str(tst) if int(i) % 2!= 0])


# Дан список:
# tst = [7, 1, 2, 5, 0, 3, 9]
# Найдите сумму элементов этого списка до первого нуля.
# tst = [7, 1, 2, 5, 0, 3, 9]
# sum = 0
# for i in tst:
#     if i == 0:
#         break
#     sum += i
# print(sum)

# print(sum(i for i in tst[:tst.index(0)]))





# Дан список:
# tst = ['a', 'b', 'c', 'd', 'e']
# Выведите в консоль значения элементов и их индексы:
# Перепишите его с помощью тернарного оператора.
# 'a1'
# 'b2'
# 'c3'
# 'd4'
# 'e5'
#
# tst = ['a', 'b', 'c', 'd', 'e']
# for index, tst in enumerate(tst):
#     print(tst, index + 1,)


# print('\n'.join(f'{tst}{i+1}' for i, tst in enumerate(tst)))



# Найдите сумму целых чисел от 1 до 100.
# a = 100
# sum = 0
# for i in range(1, a + 1):
#     sum += i
#     if i == 100:
#         break
# print("Sum :", sum)

# print(sum(range(1, 101)))



# 2 уровень сложности:
