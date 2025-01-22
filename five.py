# # #Задание: Напишите декоратор @log, который выводит имя функции и аргументы, с которыми она была вызвана.
# # # def log(func):
# # #     def wrapper(*args, **kwargs):
# # #         func(*args, **kwargs)
# # #         print(func.__name__, args, kwargs)
# # #     return wrapper
# # # @log
# # # def add(a, b):
# # #     print(a, b)
# # # add(a=5, b=11)






# # # def text_decor(func):
# # #     def wrapper(*args, **kwargs):
# # #         print("Hello")
# # #         func(*args,**kwargs)
# # #         print("Goodbye!")
# # #         return func
# # #     return wrapper
# # # @text_decor
# # # def say_name(name):
# # #     print("Alice")
# # # say_name("Alice")

# # # апишите декоратор text_decor, который оборачивает вызов декорированной функции фразами «Hello» и «Goodbye!»: 
# # # фраза «Hello» печатается до вызова, фраза «Goodbye!» — после

# # # Напишите декоратор @count_calls, который считает и выводит в консоль количество вызовов функции.

# # # def count_calls(my_args):
# # #     count_2 = 0
# # #     def wrapper(*args, **kwargs):
# # #         nonlocal count_2
# # #         count_2 += 1
# # #         print(count_2)
# # #         print('say hello!')
# # #     return wrapper
# # # @count_calls
# # # def say_hello(name):
# # #     print('LICE')
# # # say_hello('LICE')







# # Написать декоратор который будет прибавлять к аргументам функции 10

# def add_dec(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             new_args = arg + 10
#             print(new_args)
#         func(*args, **kwargs)
#     return wrapper
# @add_dec
# def string(a):
#     ...
# string(10)


# # Написать декоратор который будет проверять что в именованных аргументах 
# # функции есть аргумент с именем surname, если его нет то выводить в консоль текст "arg name not founded"
# def check_set(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         # for key, value in kwargs.items():
#         if 'surname' not in  kwargs:
#             print('arg name not founded') 
#         else:
#             print(kwargs)
#     return wrapper
    
# @check_set

# def set_user(surname, name):
#     print(surname, name)
# set_user(surname='Schon', name='oleg')
















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



