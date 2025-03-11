def wrapper_func():
    def hello_world():
        print("Hello, World!")
    return hello_world

hello_world = wrapper_func()
print(hello_world())