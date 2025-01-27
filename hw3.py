#  Программа принимает на вход список со вложенными списками
# и находит сумму элементов всех вложенных
#  списков при помощи рекурсии.

# def nested_list(lst):
#     x = 0
#     for element in lst:
#         if isinstance(element, list):
#             x += nested_list(element)
#         else:
#             x += element
#     return x
#
# nested = [1, [2,[3, 4],5],6]
# print(nested_list(nested))




# Написать функцию, которая будет вычислять число фиббоначи по его порядковому номеру
#
# def fibonacci(n):
#     if n <= 0:
#         return "Число должно быть положительным"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# n = 10
# print(fibonacci(n))



# Напишите декоратор, который будет проверять
# чётное или нечётно число возвращает функция, которую декорируем.
#  При этом функция которую декорируем получает два числа
#  в качестве аргументов и складывает их

# def my_decorator(func):
#     def wrapper(a, b):
#         if a % 2 == 0 and b % 2 == 0:
#             return func (a, b)
#         else:
#             return func(a, b)
#     return wrapper
#
# @my_decorator
# def add(a, b):
#     return a + b
#
# print(add(7, 5))
