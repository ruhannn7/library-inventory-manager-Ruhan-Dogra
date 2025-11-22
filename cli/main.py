
#again i could not get it to run in main.
import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)

from library_manager.inventory import LibraryInventory
from library_manager.book import Book


def main():
    inventory = LibraryInventory()

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book (by Title or ISBN)")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 1:
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added successfully.")

        elif choice == 2:
            if not inventory.books:
                print("No books available!")
            else:
                print("\n===== ALL BOOKS =====")
                for b in inventory.books:
                    b.display_details()

        elif choice == 3:
            isbn = input("Enter ISBN of book to issue: ")
            for b in inventory.books:
                if b.isbn == isbn:
                    b.issue_book()
                    inventory.save_books()
                    break
            else:
                print("Book not found!")

        elif choice == 4:
            isbn = input("Enter ISBN of book to return: ")
            for b in inventory.books:
                if b.isbn == isbn:
                    b.return_book()
                    inventory.save_books()
                    break
            else:
                print("Book not found!")

        elif choice == 5:
            term = input("Enter Title or ISBN to search: ")
            results = inventory.search(term)
            if results:
                for b in results:
                    b.display_details()
            else:
                print("No matching book found!")

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Enter between 1–6.")



main()