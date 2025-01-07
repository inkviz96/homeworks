# Получить с помощью вызова 2-х функциий input имя и фамилию
# и с помощью format напечатать "Hello,  !"

a = input("Enter your name: ")
b = input("Enter your lastname: ")
print("Hello, {}!".format(a + " " + b))

# Создать переменную со значением "Baloon was red. But i like blue." с помощью imput получить строку
# и попытаться найти её в созданной нами ранее переменой с помощью метода find. Без учёта регистра
# и отдельна с учётом регистра.

# Не смог, не понял, как это сделать.


# Создать 2 переменных которые будут получать значения функцией input.
# Напечатать "Sum was <сумма длин обеих строк>" с помощью f строк

a = input("Enter the first string: ")
b = input("Enter the second string: ")
print(f"Sum was {len(a) + len(b)}")


# Используя функцию count найти самую часто встречающуюся букву в тексте
# "I just returned from the greatest summer vacation! It was so fantastic, I never wanted it to end."

from collections import Counter

text = "I just returned from the greatest summer vacation! It was so fantastic, I never wanted it to end."


def most_common_letter(text):
    text = text.replace(" ", "").lower()
    letter_counts = Counter(text)
    most_common = letter_counts.most_common(1)
    return most_common[0] if most_common else None


result = most_common_letter(text)
print(f"Самая часто встречающаяся буква: '{result[0]}', встречается {result[1]} раз.")