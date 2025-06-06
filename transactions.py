# transactions.py
# Contributor: Person 3 - Book Issue/Return Management

class TransactionManager:
    def __init__(self, book_manager, user_manager):
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.transactions = []

    def issue_book(self):
        user_id = int(input("Enter user ID: "))
        book_id = int(input("Enter book ID to issue: "))

        book = next((b for b in self.book_manager.books if b['id'] == book_id), None)
        if not book:
            print("Book not found.")
            return
        if not book['available']:
            print("Book is already issued.")
            return

        book['available'] = False
        self.transactions.append({'user_id': user_id, 'book_id': book_id, 'action': 'issued'})
        print(f"Book ID {book_id} issued to User ID {user_id}.")

    def return_book(self):
        book_id = int(input("Enter book ID to return: "))

        book = next((b for b in self.book_manager.books if b['id'] == book_id), None)
        if not book:
            print("Book not found.")
            return
        if book['available']:
            print("Book is already returned.")
            return

        book['available'] = True
        self.transactions.append({'book_id': book_id, 'action': 'returned'})
        print(f"Book ID {book_id} has been returned.")

