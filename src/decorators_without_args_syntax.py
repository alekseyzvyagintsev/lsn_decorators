########### Декораторы ############

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
