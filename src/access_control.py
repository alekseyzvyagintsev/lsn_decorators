from functools import wraps

# Декоратор для контроля доступа

def access_control(role_required):
    def decorator(func):
        @wraps(func)
        def wrapper(user_role, *args, **kwargs):
            if user_role != role_required:
                raise PermissionError(f"Access denied: {role_required} role required.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Пример использования декоратора

@access_control('admin')
def delete_user(user_id):
    """Удаляет пользователя по его ID."""
    print(f"User {user_id} deleted.")

# Пример вызова функции
try:
    delete_user('admin', 123)  # Успешный вызов, так как роль совпадает
    delete_user('guest', 456)  # Ошибка доступа, так как роль не совпадает
except PermissionError as e:
    print(e)