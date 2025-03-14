def exclamation_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace("!", "!!!")
    return wrapper

def question_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace("?", "???")
    return wrapper

def dots(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace(".", "...")
    return wrapper


@exclamation_marks
@question_marks
@dots
def my_function():
    return "This is a sentence. It has a question? Does it need more exclamation!"

print(my_function())