# Week 7 Lab session
# ------------------------------------------------
# Activity 2: Simple Library Management System
# ------------------------------------------------

# Step 1: Define the classes

# Book class stores each books details 
#  such as title, author, and availability status.
class Book:
    def __init__(self, title, author):
        # Stores the book title and author
        self.title = title
        self.author = author
        self.is_available = True  # A Boolean is used to show the book availability

    def book_info(self):
        # Displays book details and availability
        status = "Available" if self.is_available else "Borrowed"
        print(f"{self.title} by {self.author} is {status}")


# Member class stores a library members name 
# and a list of books they are currently borrowing.
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # Creates a list to stores books currently borrowed by member

    def member_info(self):
        # Displays member's name and the books they are currently borrowing
        print("Member details:")
        print(f"Member: {self.name}")
        if not self.borrowed_books:
            print("No borrowed books.")
        else:
            print("Borrowed:")
            for book in self.borrowed_books:
                print(f"{book.title}")


# Library class manages the system.
# It stores books, members, and borrowing/returning operations.
class Library:
    def __init__(self):
        self.books = []    # Library collection list
        self.members = []  # Registered members list

    def add_book(self, book):
        # append adds a book to the library's collection.
        self.books.append(book)
        print(f"New book: {book.title}")    
        
    def add_member(self, member):
        # Adds the member info into the library's register
        self.members.append(member)                    
        print(f"New member: {member.name}")  

    def display_books(self):
        # Displays all books with their availability
        print("Library collection:")
        for book in self.books:
            book.book_info()

    def borrow_book(self, member, book):
        # Borrowing is only approved if the book is available
        if book.is_available:
            book.is_available = False
            member.borrowed_books.append(book)
            print(f"{member.name} borrowed '{book.title}'.")
        else:
            print(f"{member.name} attempted to borrow '{book.title}', but it is not available.")


    def return_book(self, member, book):
        # Allows returning only if the member actually borrowed the book
        if book in member.borrowed_books:
            book.is_available = True
            member.borrowed_books.remove(book)
            print(f"{member.name} returned '{book.title}'.")
        else:
            print(f"{member.name} does not have '{book.title}' borrowed.")
            

# Step 2: Test the functionality

print("\n=== LIBRARY SYSTEM TESTS ===")

# Create the library
library = Library()

print("\n=== TEST 1: ADD BOOKS TO COLLECTION ===")
# Create book objects
b1 = Book("The Secret Garden", "Frances Hodgson Burnett")
b2 = Book("Anne of Green Gables", "L.M. Montgomery")
b3 = Book("The Wind in the Willows", "Kenneth Grahame")

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

print("\n=== TEST 2: DISPLAY LIBRARY COLLECTION ===")
library.display_books()

print("\n=== TEST 3: REGISTER MEMBERS ===")
# Create member objects
m1 = Member("Sage")
m2 = Member("Juniper")
m3 = Member("Rosemary")

library.add_member(m1)
library.add_member(m2)
library.add_member(m3)

print("\n=== TEST 4: BORROW BOOKS ===")
library.borrow_book(m2, b2)   # Juniper borrows Anne of Green Gables
library.borrow_book(m2, b1)   # Juniper borrows The Secret Garden

print("\n=== TEST 5: ATTEMPT TO BORROW AN UNAVAILABLE BOOK ===")
library.borrow_book(m1, b2)   # Anne of Green Gables is already borrowed by Juniper earlier

print("\n=== TEST 6: MEMBER INFO AFTER BORROWING ===")
m2.member_info()   # Juniper
m1.member_info()   # Sage

print("\n=== TEST 7: LIBRARY COLLECTION AFTER BORROWING ===")
library.display_books()

print("\n=== TEST 8: RETURN A BOOK ===")
library.return_book(m2, b2)  # Juniper returns Anne of Green Gables

print("\n=== TEST 9: MEMBER INFO AFTER RETURNING ===")
m1.member_info()
m2.member_info()
m3.member_info()

print("\n=== TEST 10: LIBRARY COLLECTION AFTER RETURNING ===")
library.display_books()



