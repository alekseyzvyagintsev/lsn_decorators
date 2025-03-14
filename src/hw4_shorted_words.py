

def shorten_words(func):
    """
    декоратор, который берет результат декорируемой функции (текст)
    и возвращает текст, в котором каждое слово сокращено до 4 символов.
    Если слово было сокращено, в конце слова ставится точка.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return " ".join(f"{word[:4]}." if len(word) > 4 else word for word in result.split())

        # Развернутый вариант
        # words = result.split()
        # shortened_words = []
        # for word in words:
        #     if len(word) > 8:
        #         shortened_word = word[:8] + "."
        #         shortened_words.append(shortened_word)
        #     else:
        #         shortened_words.append(word)
        # return " ".join(shortened_words)
    return wrapper


@shorten_words
def text_for_tests():
    return "Каждый человек, сотворённый Богом, является решением чьей-то проблемы"

changed_text = text_for_tests()
print(changed_text)