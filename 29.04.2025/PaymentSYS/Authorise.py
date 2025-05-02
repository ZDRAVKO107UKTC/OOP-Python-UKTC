def authorize(func):
    def wrapper(self, *args, **kwargs):
        if self.CVV and self.Exp_DATE and self.Card_Number:
            print("Authorization successful.")
            return func(self, *args, **kwargs)
        else:
            print("Authorization failed: Missing payment details.")
    return wrapper
