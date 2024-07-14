class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initialize as not checked out
    
    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False  # Book is already checked out
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False  # Book is already available
    
    def is_available(self):
        return not self._is_checked_out
class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.checkout():
                    print(f"Checked out '{title}' successfully.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book with title '{title}' not found in the library.")
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}' successfully.")
                else:
                    print(f"'{title}' was already available.")
                return
        print(f"Book with title '{title}' not found in the library.")
    
    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for title in available_books:
                print(f"  {title}")
        else:
            print("No books available in the library.")
from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
