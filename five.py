# 1 уровень сложности: Программа принимает на вход список со вложенными списками и находит сумму 
# элементов всех вложенных списков при помощи рекурсии.
def sum_list(lst):
    total = 0
    for i in lst:
        if isinstance(i, list):
            total += sum_list(i)
        else:
            total += i
    return total

x = [[1,2,3],[4,5,6],[7,8,9]]
print(x)
sum_list_r = sum_list(x)
print(sum_list_r)
# Написать функцию которая будет вычислять число фиббоначи по его порядковому номеру
def func_fib(n):
    if n == 0:
        return 0
    if n == 1: 
        return 1
    return func_fib(n-1) + func_fib(n-2)
n = 4
result = func_fib(n)
print(result)



