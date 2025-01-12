# task 1
# Дан список:
# tst = [1, 2, 3, 4, 5]
# Прибавьте к его каждому элементу число 2 и выведите результат в консоль.

tst = [1, 2, 3, 4, 5]
for i in tst:
    i += 2
    print(i, end=",")
# # or
tst = [1, 2, 3, 4, 5]
print([i + 2 for i in tst])


# task 2
# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
for i in range(A, B + 1):
    if A < B:
        print(i, end= ", ")
    else:
        print("Number A must be less than B.") # не печатается ??????




# task 3
# Дан список:
# tst = [1, 2, 3, 4, 5]
# Найдите сумму квадратов элементов этого списка.

tst = [1, 2, 3, 4, 5]
print(sum(i ** 2 for i in tst))



# task 4
# Дано число:
# tst = 1234567
# Запишите из него в новый список только нечетные элементы.

tst = 1234567
new_arr = []
for num in str(tst):
    if int(num) % 2 != 0:
        new_arr.append(int(num))
print(new_arr)
# # or
print([int(num) for num in str(tst) if int(num) % 2 != 0])




# task 5
# Дан список:
# tst = [7, 1, 2, 5, 0, 3, 9]
# Найдите сумму элементов этого списка до первого нуля.
#
tst = [7, 1, 2, 5, 0, 3, 9]
Sum = 0
for i in tst:
    if i == 0:
        break
    Sum += i
print(Sum)
# # or
print(sum(i for i in tst[:tst.index(0)]))

# task 6
# Дан список:
# tst = ['a', 'b', 'c', 'd', 'e']
# Выведите в консоль значения элементов и их индексы:
# 'a1'
# 'b2'
# 'c3'
# 'd4'
# 'e5'
tst = ['a', 'b', 'c', 'd', 'e']
for index, tst in enumerate(tst):
    print("'",tst + str(index + 1),"'")


# task 7
# Найдите сумму целых чисел от 1 до 100.
print(sum(i for i in range(1,100)))

