# 1 уровень сложности: Напишите программу, которая вычисляет сумму скидки в зависимости от суммы продажи.
# Пусть скидки установлены следующим образом:
# Сумма продажи    Скидка
# 0-5000    5%
# 5000-15000    12%
# 15000-25000    20%
# свыше 25000    30%
# После вычисления скидки программа должна вывести саму скидку и сумму с вычетом скидки.

# sales_amount = float(input("Enter the sale amount: "))
# if 0 <= sales_amount < 5000:
#     discount = sales_amount * 0.05
# elif 5000 <= sales_amount < 15000:
#     discount = sales_amount * 0.12
# elif 15000 <= sales_amount < 25000:
#     discount = sales_amount * 0.20
# else:
#     discount = sales_amount * 0.30
# print(f"Discount: {discount: .2f} euro")
# print(f"Total amount after discount: {sales_amount - discount:.2f} euro")



# Дан следующий код:
# tst = 'abcdef'
# if len(tst) > 20:
#     print('string is too long')
# else:
#     print('string is too short')
# Перепишите его с помощью тернарного оператора.

# tst = len("abcdef")
# print("string is too long" if tst > 20 else "string is too short")

# 2 уровень сложности: