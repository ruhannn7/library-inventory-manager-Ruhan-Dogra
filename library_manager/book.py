class Book:
    def __init__(self, title, author, isbn, status='Available'):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def display_details(self):
        print("\n--- Book Details ---")
        print(f"TITLE : {self.title}")
        print(f"AUTHOR: {self.author}")
        print(f"ISBN  : {self.isbn}")
        print(f"STATUS: {self.status}")

    def is_available(self):
        return self.status == "Available"

    def issue_book(self):
        if self.is_available():
            self.status = "Issued"
            print(f"SUCCESS: '{self.title}' has been successfully issued.")
        else:
            print(f"FAILURE: '{self.title}' is already {self.status}.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print(f"SUCCESS: '{self.title}' has been returned.")
        else:
            print(f"FAILURE: '{self.title}' was not issued.")
