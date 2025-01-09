# Напишиите программу, которая вычисляет сумму скидки в зависимости от суммы продажи.
# Пусть скидки установлены следующим образом:
# Сумма продажи    Скидка
# 0-5000    5%
# 5000-15000    12%
# 15000-25000    20%
# свыше 25000    30%
# После вычисления скидки программа должна вывести саму скидку и сумму с вчетом скидки.

your_sum = int(input())
if your_sum < 5000:
    b = your_sum * 0.05
    a = your_sum - b
if 5000 <= your_sum < 15000:
    b = your_sum * 0.12
    a = your_sum - b
if 15000 <= your_sum < 25000:
    b = your_sum * 0.2
    a = your_sum - b
if your_sum > 25000:
    b = your_sum * 0.3
    a = your_sum - b
print(f"Your check = {your_sum}\nYour discount = {b}\nTotal amount = {a}")


# task 2
# Дан следующий код:
# tst = 'abcdef'
# if len(tst) > 20:
#     print('string is too long')
# else:
#     print('string is too short')
# Перепишите его с помощью тернарного оператора.
tst = 'abcde'
msg1 = 'string is too long'
msg2 = 'string is too short'
print(msg1 if len(tst) > 20 else msg2)

