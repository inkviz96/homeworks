#tst = [1,2,3,4,5]
#for a in tst:
 #   print(a+2)

#tst = [1,2,3,4,5]
#print(sum(a**2 for a in tst))

#A, B = map(int, input().split())
#for i in range(A, B + 1):
 #   print(i)

tst = 1234567
odd_digits = [int(digit) for digit in str(tst) if int(digit) % 2 != 0]
print(odd_digits)

tst = [7, 1, 2, 5, 0, 3, 9]
a = 0
for num in tst:
    if num == 0:
        break
    a += num
print(a)
tst = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(tst, start=1):
    print(f"{value}{index}")

n = 100
sum_numbers = n * (n + 1)// 2
print(sum_numbers)
