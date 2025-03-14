####################### Пример использования ########################
from time import time

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