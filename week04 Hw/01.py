class Book:
    def __init__(self, title, genre, publication_year, price):
        self.title = title
        self.genre = genre
        self.publication_year = publication_year
        self.price = price
    
    def display_book_info(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Price: ${self.price:.2f}")
    
    def calculate_discount(self):
        if 2017 <= self.publication_year <= 2021:
            return self.price * 0.05
        elif self.publication_year > 2021:
            return 0
        else:
            return 0

book1 = Book("War and Peace", "Roman", 1995, 500)
book2 = Book("To Kill a Mockingbird", "Fiction", 1960, 450)
book3 = Book("The Great Gatsby", "Novel", 1925, 200)
book4 = Book("The Good Life", "Novel", 2019, 400)
book5 = Book("The Baffold", "Drama", 2020, 660)
book6 = Book("The Smile", "Fantasy", 2020, 700)

books = [book1, book2, book3, book4, book5, book6]

for book in books:
    book.display_book_info()
    print(f"Discount: ${book.calculate_discount():.2f}")
    print("------------------------------------------")

def delete_book():
    title = input("Enter the title of the book you want to delete: ")
    price = float(input("Enter the price of the book you want to delete: "))
    for book in books:
        if book.title == title and book.price == price:
            books.remove(book)
            print(f"{title} has been deleted.")
            return
    print(f"{title} not found.")

def average_price():
    if not books:
        return 0
    total_price = sum(book.price for book in books)
    return total_price / len(books)

print(f"Average price of all books: ${average_price():.2f}")

delete_book()

print("\nUpdated list of books:")
for book in books:
    book.display_book_info()
    print("------------------------------------------")

