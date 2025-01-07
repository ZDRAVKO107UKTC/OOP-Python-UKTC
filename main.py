# class Calculator:
#     @staticmethod
#     def square(n):
#         return n * n
#
# print(Calculator.square(8))
#
# class String_Utils:
#     @staticmethod
#     def reverse_string(s):
#         return s[::-1]
#
# print(String_Utils.reverse_string(input()))

# class Person:
#     def __init__(self, age):
#         self.age = age
#/
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
# age = int(input())
# perso = Person.is_adult(age)
# print(perso)

class book_store:
    def __init__(self):
        self.books = {}


    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        publication_year = int(input("Enter book publication year: "))
        self.books[title] = {"author": author, "publication_year": publication_year}

    def borrow(self):
        title = input("Enter book title to borrow: ")
        if title in self.books:
            print(f"You have borrowed {title}.")
            del self.books[title]
        else:
            print("Book not found.")

    def display_books(self):
        for title, details in self.books.items():
            print(f"Title: {title}")
            print(f"Author: {details['author']}")
            print(f"Publication Year: {details['publication_year']}")
            print("-------------------------")

    def return_books(self):
        title = input("Enter book title to return: ")
        if title in self.books:
            print(f"You have returned {title}.")
            self.books[title] = {"author": "", "publication_year": 0}
        else:
            print("Book not found.")



store = book_store()
while True:
    print("\n1. Add Book")
    print("2. Borrow Book")
    print("3. Display Books")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice < 1 or choice > 5:
        print("Invalid choice. Please try again.")
        continue

    if choice == 1:
        store.add_book()
    elif choice == 2:
        store.borrow()
    elif choice == 3:
        store.display_books()
    elif choice == 4:
        store.return_books()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
