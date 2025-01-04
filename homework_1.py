# task 1
# Получить с помощью вызова 2-х функциий input имя и фамилию
# и с помощью format напечатать "Hello,  !"

name = input()
surname = input()
print("\"Hello, {} {} !\"".format(name, surname))


# task 2
# Создать 2 переменных которые будут получать значения функцией input.
# Напечатать "Sum was <сумма длин обеих строк>" с помощью f строк

length_1 =float(input())
length_2 =float(input())
print(f"\"Sum was {sum([length_1,length_2])}\"")


# task 3
# Создать переменную со значение "Baloon was red. But i like blue."
# с помощью imput получить строку и попытаться найти её в созданной нами ранее переменой
# с помощью метода find. Без учёта регистра и отдельна с учётом регистра.

text = "Baloon was red. But i like blue."
substring = input()
print(text.find(substring))


# task 4
# Используя функцию count найти самую часто встречающуюся букву в тексте
# "I just returned from the greatest summer vacation! It was so fantastic,
# I never wanted it to end."

text = '''"I just returned from the greatest summer vacation! 
It was so fantastic,  I never wanted it to end."'''
char = input()
print(text.count(char)) # t = 12
