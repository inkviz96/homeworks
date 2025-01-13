


tst = [1, 2, 3, 4, 5]
for x in tst:
    print(x + 2)
A = 3
B = 7
for i in range(A, B + 1):
    print(i)
tst = [1, 2, 3, 4, 5]
result = 0
for x in tst:
    result += x ** 2
print(result)
tst = 1234567
result = []
for digit in str(tst):
    if int(digit) % 2 != 0:
        result.append(int(digit))
print(result)

tst = [7, 1, 2, 5, 0, 3, 9]
result = 0
for x in tst:
    if x == 0:
        break
    result += x
print(result)

tst = ['a', 'b', 'c', 'd', 'e']
index = 1
for value in tst:
    print(value + str(index))
    index += 1

result = 0
for i in range(1, 101):
    result += i
print(result)


