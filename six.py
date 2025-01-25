#  1 уровень сложности: напишите декоратор который будет проверять чётное или нечётно число возвращает
#   функция которую декорируем. 
#  При этом функция которую декорируем получает два числа в качестве аргументов и складывает их



def dec_chet_nechet(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 == 0:
            print('Четное')
            return True
        else:
            print('Нечетное')
            return False
    return wrapper


@dec_chet_nechet
def sum_int(*args):
    a = int(input())
    b = int(input())
    return sum([a,b])
sum_int()