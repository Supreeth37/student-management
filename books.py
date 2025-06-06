# books.py
# Contributor: Person 1 - Book Management

class BookManager:
    def __init__(self):
        self.books = []
        self.book_id_counter = 1

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")

        book = {
            'id': self.book_id_counter,
            'title': title,
            'author': author,
            'year': year,
            'available': True
        }
        self.books.append(book)
        print(f"Book '{title}' added with ID {self.book_id_counter}.")
        self.book_id_counter += 1

    def view_books(self):
        if not self.books:
            print("No books in the system.")
            return

        print("\nAvailable Books:")
        for book in self.books:
            status = "Available" if book['available'] else "Issued"
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['year']} | Status: {status}")
# books.py
# Contributor: Person 1 - Book Management

class BookManager:
    def _init_(self):
        self.books = []
        self.book_id_counter = 1

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")

        book = {
            'id': self.book_id_counter,
            'title': title,
            'author': author,
            'year': year,
            'available': True
        }
        self.books.append(book)
        print(f"Book '{title}' added with ID {self.book_id_counter}.")
        self.book_id_counter += 1

    def view_books(self):
        if not self.books:
            print("No books in the system.")
            return

        print("\nAvailable Books:")
        for book in self.books:
            status = "Available" if book['available'] else "Issued"
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['year']} | Status: {status}")
