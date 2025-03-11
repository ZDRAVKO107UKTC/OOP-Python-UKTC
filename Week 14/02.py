def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        func()
        print(f"After calling {func.__name__}")
    return wrapper

@my_decorator
def my_function():
    print("Inside my_function")

my_function()