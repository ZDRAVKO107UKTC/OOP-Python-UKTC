def log_action(func):
    def wrapper(*args, **kwargs):
        item = args[0]
        print(f"[LOG] Подготовка започва за: {item.name}")
        result = func(*args, **kwargs)
        print(f"[LOG] Подготовката на {item.name} завърши.")
        return result
    return wrapper