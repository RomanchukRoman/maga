from functools import wraps

def uppercase_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper


# Пример
@uppercase_output
def greeting():
    return "hello"

@uppercase_output
def get_number(): 
    return 42

print(greeting())  # "HELLO"
print(get_number()) # 42
