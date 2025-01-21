from datetime import datetime

class Book:
    def __init__(self, title: str, author: str, year: int, copies: int):
        self.title = title
        self.author = author

        if not self.checkYear(year):
            raise TypeError("A year should be a 4-digit number and not bigger than the current one.")
        self.year = year

        if not copies.is_integer():
            raise TypeError("A number of copies should be... a number.")
        self.copies = copies
    
    @staticmethod
    def checkYear(year: int) -> bool:
        '''Checks if year is a 4-digit number not larget than the current year'''
        try:
            int(year)
        except:
            return False
        if len(str(year)) == 4 and year <= datetime.now().year:
            return True
        else:
            return False

    def borrow_book(self) -> bool:
        '''Borrows a new book and decrease its number of copies by 1'''
        if self.copies > 0:
            self.copies -= 1
            print("Successfully borrowed a book.")
            return True
        else:
            print("There was no available copy of this book.")
            return False

    def return_book(self) -> bool:
        '''Returns a book and increases number of its copies by 1'''
        if len(self.copies) > 0:
            self.copies += 1
            print("Successfully returned a book")
            return True
        else:
            print("You don't have any borrowed book.")
            return False
    
    def display_details(self) -> str:
        '''Display book in this order: Title; Author; Year; Copies'''
        print(f"Title: {Colors.VAR}{self.title}{Colors.ENDC}; Author: {Colors.VAR}{self.author}{Colors.ENDC}; Year: {Colors.VAR}{self.year}{Colors.ENDC}; Copies: {Colors.VAR}{self.copies}{Colors.ENDC}\n")

class Reader:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.borrowed_books = []
    
    def borrow(self, book: str) -> bool:
        '''Borrows book for a reader if borrowed books doesn't exceed limit of 5 and reader hasn't borrowed it already.'''
        if len(self.borrowed_books) > 5:
            print("You cannot have more than 5 borrowed books at a time.")
            return False

        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            print("Book borrowed successfully.\n")
            return True
        else:
            print("You have already borrowed that book.\n")
            return False
    
    def return_book(self, book: str) -> str:
        '''Returns book if reader has borrowed it.'''
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print("Book returned successfully.\n")
        else:
            print("You haven't borrowed that book.\n")
    
    def display_borrowed_books(self) -> str:
        '''Displays borrowed books.'''
        print(f"Borrowed books of {Colors.VAR}{self.first_name} {self.last_name}{Colors.ENDC}:")

        book_number = 1
        for book in self.borrowed_books:
            print(f"Book {book_number}: {Colors.VAR}{book}{Colors.ENDC}\n")
            book_number += 1
    
class PremiumReader(Reader):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.borrowed_books = []
    
    def can_borrow_more(self) -> bool:
        '''Checks if reader can borrow more books. If yes, it tells how many books he can still borrow.'''
        if len(self.borrowed_books) < 10:
            print(f"You can borrow {10 - len(self.borrowed_books)} books more.\n")
            return True
        else:
            print("You cannot borrow more books at this moment. Your limit it 10 books.\n")
            return False
    
    def borrow_exclusive(self, book: str):
        pass

class Library:
    def __init__(self):
        self.books_list = []
        self.readers_list = []
    
    def add_book(self, book: str):
        '''Adds book to library from Book class object.'''
        self.books_list.append(book)
    
    def add_reader(self, reader):
        '''Adds reader to library from Reader class object.'''
        self.readers_list.append(reader)
    
    def display_books(self):
        '''Displays all books created with Book class and added to library.'''
        for book in self.books_list:
            Book.display_details(book)
    
    def display_readers(self):
        '''Displays all readers created with Reader class and added to library.'''
        for reader in self.readers_list:
            Reader.display_borrowed_books(reader)

class Colors:
    VAR = '\033[93m'
    ENDC = '\033[0m'

def main():
    book_one = Book("Hobbit", "J.R.R Tolkien", 1996, 10)
    book_one.display_details()

    book_two = Book("Władca Pierścieni", "J.R.R Tolkien", 2000, 20)
    book_two.display_details()

    reader_one = Reader("Jan", "Brzechwa")
    reader_one.borrow("Hobbit")
    reader_one.display_borrowed_books()

    reader_two = Reader("Cezary", "Pazura")
    reader_two.borrow("Hobbit")
    reader_two.borrow("Władca Pierścieni")
    reader_two.return_book("Hobbit")
    reader_two.display_borrowed_books()

    library = Library()
    library.add_book(book_one)
    library.add_book(book_two)
    library.add_reader(reader_one)
    library.add_reader(reader_two)

    library.display_books()
    library.display_readers()

if __name__ == "__main__":
    main()