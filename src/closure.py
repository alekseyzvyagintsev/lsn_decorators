####### Замыкания #########

# Внешняя функция
def create_counter():
    """создаем переменную именно в виде списка,
    чтобы его можно было бы изменить
    и сохранить значение для беспрерывной работы счетчика.
    Чтобы он не обнулялся каждый раз"""
    count:  list[int] = [0]

    # Внутренняя функция
    def counter() -> int:
        count[0] += 1
        return count[0]

    # Возвращаем ссылку на внутреннюю функцию
    return counter # имя функции без скобок

# Создаем замыкание
my_counter = create_counter()
print(my_counter())
print(my_counter())
print(my_counter())
print(my_counter())
print(my_counter())
print(my_counter())


# Внешняя функция принимает параметр x
def make_multiplier(x):

    # Внутренняя функция использует значение x из внешней функции
    def multiplier(y):
        return x * y

    # Возвращаем внутреннюю функцию
    return multiplier

# Создаем замыкание
double = make_multiplier(2)
print(double(5))

