def validate_data(func):
    def wrapper(self, *args, **kwargs):
        if not self.name or self.age < 0 or not self.diagnosis:
            print(f"[ERROR] Invalid data for {self.__class__.__name__}.")
            return
        return func(self, *args, **kwargs)
    return wrapper
