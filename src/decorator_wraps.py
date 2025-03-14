from functools import wraps # Импортируем декоратор wraps

def checking_that_arg_is(predicate, error_message):
    def wrapper(function):
        @wraps(function)
        def inner(arg):
            if not predicate(arg):
                raise ValueError(error_message)
            return function(arg)
        return inner
    return wrapper


############################# Предикаты #############################
def predicate_is_int(x):
    return type(x) == int


def predicate_is_positive(x):
    return x > 0


################ пример использования декоратора wraps ##################
@checking_that_arg_is(predicate_is_int, "Должно быть целое число")
@checking_that_arg_is(predicate_is_positive, "Число должно быть больше нуля")
def square(value):
    """ Возведение числа в квадрат"""
    return value ** 2

help(square)         # help выдаст описание
# Или так
print(help(square))  # help выдаст описание, а print выдаст None