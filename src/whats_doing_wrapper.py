# Определяем функцию-декоратор
import sys


def my_decorator(func):
    def wrapper():
        print("Перед вызовом функции.")
        func()  # Здесь вызывается исходная функция
        print("После вызова функции.")
    return wrapper  # Возвращаем функцию wrapper

# Применяем декоратор к функции
@my_decorator
def say_hello():
    print("Hello!")

# Вызываем декорированную функцию
say_hello()



####################### как использовать capsys ########################
def greeting(name):
    print('Hi, {}'.format(name))
    """
    Вы не можете проверить это, проверив возвращаемое значение. 
    Вы должны как-то проверить stdout. 
    Вы можете проверить результат с помощью caps:
    """


def test_greeting(capsys):
    greeting('Earthling')
    out, err = capsys.readouterr()
    assert out == 'Hi, Earthling\n'
    assert err == ''

    greeting('Brian')
    greeting('Nerd')
    out, err = capsys.readouterr()
    assert out == 'Hi, Brian\nHi, Nerd\n'
    assert err == ''
    """
    Захваченные stdout и stderr извлекаются из capsys.redouterr(). 
    Возвращаемое значение — это то, что было зафиксировано с начала функции, 
    или с момента последнего вызова.

    В предыдущем примере используется только stdout. 
    Давайте посмотрим на пример, используя  поток stderr:
    """

def yikes(problem):
    print('YIKES! {}'.format(problem), file=sys.stderr)

def test_yikes(capsys):
    yikes('Out of coffee!')
    out, err = capsys.readouterr()
    assert out == ''
    assert 'Out of coffee!' in err