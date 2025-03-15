import pytest
import time

######################### Вариант простого декоратора ########################

# def retry(func):
#     """
#     декоратор, который повторно вызывает декорируемую функцию три раза.
#     Каждый раз через три секунды, если произошла ошибка.
#     """
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             try:
#                 return func(*args, **kwargs)
#             except:
#                 time.sleep(3)
#         raise Exception('Function call failed after multiple retries.')
#     return wrapper


# @retry
# def multiply():
#     x = int(input("введите число для умножения - "))
#     res = x * 2
#     return res
#
# print(multiply())


######################### Вариант декоратора с параметрами ########################
def retry_decorator(max_retry):
    def retry(func):
        """
        декоратор, который повторно вызывает декорируемую функцию три раза.
        Каждый раз через три секунды, если произошла ошибка.
        """
        def wrapper(*args, **kwargs):
            for i in range(max_retry):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Попробуйте еще раз... ({e})")
                    time.sleep(1)
            raise Exception("Все попытки исчерпаны")
        return wrapper
    return retry

@retry_decorator(max_retry=3)
def multiply():
    x = int(input("введите число для умножения - "))
    res = x * 2
    return res


########################### Тест декоратора ###########################

if __name__ == '__main__':
    with pytest.raises(Exception, match="Все попытки исчерпаны"):
        multiply()