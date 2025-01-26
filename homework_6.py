# Напишите декоратор который будет проверять чётное или нечётно число возвращает функция
# которую декорируем. При этом функция которую декорируем получает два числа в качестве
# аргументов и складывает их

def decorator(func):
    def wrapper(a,b):
        value = func(a, b)
        if value % 2 == 0:
            print(f"The number {value} is even")
        else:
            print(f"The number {value} is odd")
        return value
    return wrapper

@decorator
def sum_num(a, b):
    return a + b
sum_num(8, 8)



