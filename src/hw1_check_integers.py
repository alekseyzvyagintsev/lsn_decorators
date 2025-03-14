
def check_integers(func):
    """
    декоратор, который проверяет, что все числа,
    возвращаемые декорируемой функцией, являются целыми,
    и округляет их до целых, если это не так.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if type(result) == float:
            return round(result)
        elif type(result) in (list, tuple):
            rounded = [round(x) if type(x) == float else x for x in result]
            # Возвращаем тот же тип, что и исходный (list или tuple)
            return type(result)(rounded)
        else:
            return result

    return wrapper


@check_integers
def nums_gen():
    num_list = []
    for n in range(10):
        num_list.append(n / 3)
    return num_list


print(nums_gen())