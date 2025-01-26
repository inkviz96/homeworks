# Программа принимает на вход список со вложенными списками и
# находит сумму элементов всех вложенных списков при помощи рекурсии.

def sum_element(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum_element(element)
        else:
            total = total + element
    return total
print(sum_element([[1, 7], 4, [3, 15]]))

# Написать функцию которая будет вычислять число фиббоначи по его порядковому номеру

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(15))