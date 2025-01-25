class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def input_info(self):
        self.title = input("Въведете заглавие: ")
        self.author = input("Въведете автор: ")
        self.year = input("Въведете година на издаване: ")

    def display_info(self):
        print(f"Заглавие: {self.title}, Автор: {self.author}, Година: {self.year}")


class Book(Publication):
    def __init__(self, title, author, year, number):
        super().__init__(title, author, year)
        self.number = number

    def display_info(self):
        super().display_info()
        print(f"Номер: {self.number}")


class Magazine(Publication):
    def __init__(self, title, author, year, code):
        super().__init__(title, author, year)
        self.code = code

    def display_info(self):
        super().display_info()
        print(f"Код: {self.code}")


# Създаване на обекти от подкласовете
book1 = Book("1984", "Джордж Оруел", 1949, "12345")
book2 = Book("Мобидик", "Херман Мелвил", 1851, "67890")

magazine1 = Magazine("National Geographic", "Various", 2023, "NG2023")
magazine2 = Magazine("Time", "Various", 2023, "TIME2023")

# Извеждане на информацията
print("Информация за книги:")
book1.display_info()
book2.display_info()

print("\nИнформация за списания:")
magazine1.display_info()
magazine2.display_info()