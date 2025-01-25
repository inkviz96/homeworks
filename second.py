# Создать переменную со значение "Baloon was red. But i like blue." 
# с помощью imput получить строку и попытаться найти её в созданной
# нами ранее переменой с помощью метода find. Без учёта регистра и отдельна с учётом регистра.

# Создать 2 переменных которые будут получать значения функцией input.
# Напечатать "Sum was <сумма длин обеих строк>" с помощью f строк

# Используя функцию count найти самую часто встречающуюся букву в тексте
# "I just returned from the greatest summer vacation! It was so fantastic, I never wanted it to end."

#(1)
j = 'Baloon was red. But i like blue.'
k = input(': ')
print(j.find(k))
print(j.lower().find(k))
#(2)
h = len(input())
g = len(input())
print(f"Sum was {h+g}")

#(3)
t = "I just returned from the greatest summer vacation! It was so fantastic, I never wanted it to end."
t = t.lower()

m_str = ''

maxi = 0

for a in set(t):

    count = t.count(a)

    if count > maxi and a != ' ':

        m_str = a
        maxi = count

print(f"most letter = {m_str}, sum = {maxi}")
