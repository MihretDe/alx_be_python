# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book: {self.title} by {self.author}"

    def __str__(self):
        return self.get_details()


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __str__(self):
        return self.get_details()


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __str__(self):
        return self.get_details()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)  # __str__() is used automatically
