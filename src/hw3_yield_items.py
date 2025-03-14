# def yield_items(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         # Проверка на тип с использованием type()
#         if type(result) in (list, tuple):
#             for item in result:
#                 yield item
#         else:
#             yield result
#     return wrapper
#
#
# @yield_items
# def nums_gen():
#     num_list = []
#     for n in range(10):
#         num_list.append(n)
#     return num_list
#
#
# numbers = nums_gen()
# print(next(numbers))

def yield_items(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result type: {type(result)}")  # Добавляем отладочный вывод
        if type(result) in (list, tuple):
            for item in result:
                yield item
        else:
            yield result
    return wrapper

# Функция, возвращающая список

@yield_items
def nums_gen() -> iter:
    num_list = []
    for n in range(10):
        num_list.append(n)
    return num_list

# Создаем объект генератора

numbers = nums_gen()

# Используем next() на объекте генератора

print(next(numbers))  # Печатает первый элемент
print(next(numbers))  # Печатает второй элемент
print(next(numbers))
print(next(numbers))
print(next(numbers))