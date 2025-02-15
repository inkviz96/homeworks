def check_even_odd(func):
    def wrapper(a, b):
        result = func(a, b)
        if result % 2 == 0:
            print(f"Результат {result} — чётное число.")
        else:
            print(f"Результат {result} — нечётное число.")
        return result
    return wrapper

@check_even_odd
def add_numbers(a, b):
    return a + b


add_numbers(3, 4)
add_numbers(2, 4)