def fibonacci(n):
    if n <= 0:
        return "Номер должен быть положительным числом."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 10
result = fibonacci(n)
print(f"Число Фибоначчи с номером {n} равно {result}.")
