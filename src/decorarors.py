########### Декораторы ############
from time import time


######################################################################
def Bolvanka(func):
    """
    Это болванка декоратора никак не меняющая поведение оборачиваемой функции,
    принимающая на вход все возможные параметры,
    возврвщающая результат оборачивания.
    """
    def wrapper(*args, **kwargs):
        print(f'Здесь код перед вызовом обертываемой функции если нужно')
        result = func(*args, **kwargs)
        print(f'Здесь код после вызова обертываемой функции если нужно')
        return result

    return wrapper

#######################################################################

def printing(func):

    def wrapper(*args, **kwargs):
        print(f'Функция printing стартовала')
        result = func(*args, **kwargs)
        print(f'Функция printing завершилась')
        print()
        return result

    return wrapper


# Функция таймер работы функции
def timer(func):

    def wrapper(*args, **kwargs):
        print("Тамер стартовал")
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        print(f'Время работы функции {time_2 - time_1}')
        return result

    return wrapper

@timer
@printing
def example():
    for i in range(10):
        continue


example()