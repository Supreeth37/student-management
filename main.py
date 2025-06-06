# main.py
# Owner: Repository Maintainer

from books import BookManager
from users import UserManager
from transactions import TransactionManager

def main():
    book_manager = BookManager()
    user_manager = UserManager()
    transaction_manager = TransactionManager(book_manager, user_manager)

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Register User")
        print("4. View Users")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_manager.add_book()
        elif choice == '2':
            book_manager.view_books()
        elif choice == '3':
            user_manager.register_user()
        elif choice == '4':
            user_manager.view_users()
        elif choice == '5':
            transaction_manager.issue_book()
        elif choice == '6':
            transaction_manager.return_book()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

