# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out if not already."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                break

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                break

    def list_available_books(self):
        """Print all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
