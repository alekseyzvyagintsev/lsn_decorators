import time

def retry(func):
    """
    декоратор, который повторно вызывает декорируемую функцию три раза.
    Каждый раз через три секунды, если произошла ошибка.
    """
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except:
                time.sleep(3)
        raise Exception('Function call failed after multiple retries.')
    return wrapper


@retry
def multiply():
    x = int(input("введите число для умножения - "))
    res = x * 2
    return res

print(multiply())