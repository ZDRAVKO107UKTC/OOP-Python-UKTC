class book:
    def __init__(self, title, author, number):
        self.__title = title
        self.__author = author
        self.__number = number

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Number of Pages: {self.__number}"

title01 = input("Enter a title: ")
author01 = input("Enter a author: ")
number01 = int(input("Enter a number of pages: "))
book01 = book(title01, author01, number01)

title02 = input("\nEnter a title: ")
author02 = input("Enter a author: ")
number02 = int(input("\nEnter a number of pages: "))
book02 = book(title02, author02, number02)

print(book01)
print(book02)