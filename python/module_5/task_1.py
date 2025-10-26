from functools import wraps

def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
        

@call_counter
def greet(name):
    return f"Hello, {name}"

greet("Alice")
greet("Bob")
greet("Bob")
print(greet.calls)  # 3
print(greet.__name__)
