from functools import wraps

import pytest


def checking_that_arg_is(predicate, error_message):
    def wrapper(function):
        @wraps(function)
        def inner(arg):
            if not predicate(arg):
                raise ValueError(error_message)
            return function(arg)
        return inner
    return wrapper


########################## Предикаты ##########################

def greater_than(value):
    def predicate(arg):
        return arg > value
    return predicate


def in_(*values):
    def predicate(arg):
        return arg in values
    return predicate


def not_(other_predicate):
    def predicate(arg):
        return not other_predicate(arg)
    return predicate


def predicate_is_int(x):
    return type(x) == int


def predicate_is_positive(x):
    return x > 0


######################### пример использования без предикатов ##########################

@checking_that_arg_is(lambda x: x > 0, "Value must be greater than 0!")
def example_function(value):
    """ Функция умножения на 2"""
    return value * 2

# print(example_function(1))

########################### пример использования с предикатами ############################

@checking_that_arg_is(greater_than(0), "Non-positive!")
@checking_that_arg_is(not_(in_(5, 15, 42)), "Bad value!")
def foo(arg):
    return arg


# print(foo(int(example_function(22))))


@checking_that_arg_is(predicate_is_int, "Должно быть целое число")
@checking_that_arg_is(predicate_is_positive, "Число должно быть больше нуля")
def square(value):
    """ Возведение числа в квадрат"""
    return value ** 2


# print(help(square))
# print(example_function(1))
# print(example_function("1"))
# print(example_function(-1))


########################### Тест декоратора ###########################

if __name__ == '__main__':
    # Тест на выбрасывание ошибки декоратором совместно с конкретным предикатором
    with pytest.raises(ValueError, match="Число должно быть больше нуля"):
        square(-3)

    # Тест на то, что декоратор отрабатывает декорируемую функцию если не выпала ошибка предикатора
    assert square(3) == 9

    # Тест работы предикатора
    assert predicate_is_positive(3) == True