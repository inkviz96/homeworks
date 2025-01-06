## Темы: Операции над строками, Индексы и срезы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Объедините строки "Hello" и "London" без пробела. Ожидаемый результат: "HelloLondon"


# 2. Выведите последний символ строки "Programming". Ожидаемый результат: "g"


# 3. Дублируйте строку "Hi" три раза. Ожидаемый результат: "HiHiHi"


# 4. Определите длину строки "Artificial Intelligence".


# 5. Объедините строки "Good" и "Morning" с запятой между ними. Ожидаемый результат: "Good,Morning"


# 6. Создайте срез строки "Natural Language Processing" со значением "nguag".


# 7. Объедините строки "Data" и "Science" с дефисом между ними. Ожидаемый результат: "Data-Science"


# 8. Объедините строки "AI" и "ML" с двоеточием между ними. Ожидаемый результат: "AI:ML"


# 9. Дублируйте строку "Test" шесть раз. Ожидаемый результат: "TestTestTestTestTestTest"


# 10. Выведите первый символ строки "Python". Ожидаемый результат: "P"


# 11. Создайте срез строки "Hello, Anna!" от 0 до 5. Ожидаемый результат: "Hello"


# 12. Определите длину строки "Natural Language Processing".


# 13. Выведите второй символ строки "Лето". Ожидаемый результат: "е"


# 14. Выведите предпоследний символ строки "Machine Learning". Ожидаемый результат: "n"


# 15. Дублируйте строку "Yes" четыре раза. Ожидаемый результат: "YesYesYesYes"


# 16. Создайте срез строки "Deep Learning" со значением "ep Le".


# 17. Выведите третий символ строки "Computer Vision". Ожидаемый результат: "m"


# 18. Определите длину строки "Deep Learning". Ожидаемый результат: 13


# 19. Объедините строки "Python" и "Rocks" с пробелом между ними. Ожидаемый результат: "Python Rocks"


# 20. Создайте срез строки "Data Science" со значением "cien".



j = 'Hello'
k = 'London'
print(j+k)#1

k = "Programming"
print(k[-1])#2

l = 'Hi'
print(l*3)#3

p = "Artificial Intelligence"
print(len(p))#4

s = 'Good'
f = 'Morning'
print(s,f, sep=',')#5

io = "Natural Language Processing"
print(io[10:15])#6

d = 'Data'
t = 'Science'
print(d, t, sep='-')#7

rt = 'AI'
tr = 'ML'
print(rt, tr, sep=':')#8

test = 'Test'
print(test*6)#9

po = 'Python'
print(po[0])#10

ha = 'Hello, Anna'
print(ha[0:5])#11

nds = "Natural Language Processing"
print(len(nds))#12

somm = 'Лето'
print(somm[1])#13

ml = "Machine Learning"
print(ml[-2])#14

re = "Yes"
print(re*4)#15

dl = 'Deep Learning'
print(dl[2:7])#16

clp = "Computer Vision"
print(clp[2])#17

print(len(dl))#18

gh = "Python" 
fgh = "Rocks" 
print(gh, fgh)#19

hj = "Data Science"
print(hj[6:10])#20

