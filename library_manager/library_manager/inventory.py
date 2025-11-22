import os
from .book import Book
#Dear mam, I could not get this to run in main so i had to use help to make it run.
BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, "library.txt")


class LibraryInventory:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()

    def save_books(self):
        """Save all books to library.txt."""
        try:
            with open(FILE_PATH, "w") as f:
                for book in self.books:
                    line = f"{book.title},{book.author},{book.isbn},{book.status}\n"
                    f.write(line)
        except Exception as e:
            print("Error saving file:", e)

    def load_books(self):
        if not os.path.exists(FILE_PATH):
            return

        try:
            with open(FILE_PATH, "r") as f:
                for line in f:
                    clean = line.rstrip("\n")     
                    parts = clean.split(",")
                    if len(parts) == 4:
                        title, author, isbn, status = parts
                        self.books.append(Book(title, author, isbn, status))
        except Exception as e:
            print("Error loading file:", e)

    def search(self, term):
        term_lower = term.lower()
        results = []
        for b in self.books:
            if b.title.lower() == term_lower or b.isbn == term:
                results.append(b)
        return results