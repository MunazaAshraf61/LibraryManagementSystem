import csv

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name):
        self.name= name

    @abstractmethod
    def display_details(self):
        pass


class Student(Person):
    def __init__(self,name,student_id):
        super().__init__(name)
        self.student_id=student_id

    def display_details(self):
        print(f"Student's name:{self.name}")
        print(f"Student's id:{self.student_id}")



class Book:
    def __init__(self, book_id, title, author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.available = True

    def display_details(self):
        print(f"book{self.book_id} titled'{self.title}' has written by {self.author}")



class Library:
    def __init__(self):
        self.books = []
        self.students = []

    #add a book to the library
    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print("A book with this ID already exists.")
                return
    
        self.books.append(book)
        print("Book has been added.")

    #display all available books
    def display_available_books(self):
        if not self.books:
            print("No books have been added to the library.")
            return

        found = False

        for book in self.books:
            if book.available:
                book.display_details()
                print("--------------------")
                found = True

        if not found:
            print("No books are currently available.")

    
    #search book
    def search_book(self, book_id):
        for book in self.books:
            if book_id == book.book_id:
                book.display_details()
                return

        print("Book was not found.")

    #issue book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book has been issued.")
                else:
                    print("Book is already issued.")
                return

        print("Book was not found.")

    
    #return book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book has been returned.")
                else:
                    print("Book was not issued.")
                return

        print("Book was not found.")

    
    #save books to a CSV file
    def save_books(self):
        try:
            with open("books.csv", "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow([
                    "book_id", "title", "author", "available"
                ])

                for book in self.books:
                    writer.writerow([
                        book.book_id,
                        book.title,
                        book.author,
                        book.available
                    ])

        except OSError as error:
            print(f"Error saving books: {error}")


    
    #load books from a CSV file
    def load_books(self):
        try:
            with open("books.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                # Loop through each row in the CSV file
                for row in reader:

                    # Create a Book object for each row
                    book = Book(
                        int(row["book_id"]),
                        row["title"],
                        row["author"]
                    )

                    # Restore the book's availability
                    book.available = row["available"] == "True"

                    # Add the book to the library
                    self.add_book(book)

        except FileNotFoundError:
            print("No saved books found. Starting with an empty library.")



# Main menu
library = Library()
library.load_books()

while True:
    print("\n===== Library Management System =====")
    print("1. Add a book")
    print("2. Display available books")
    print("3. Search for a book")
    print("4. Issue a book")
    print("5. Return a book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        try:
            book_id = int(input("Enter book ID: "))
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()

            if not title or not author:
                print("Book title and author cannot be empty.")
                continue

            book = Book(book_id, title, author)
            library.add_book(book)
            library.save_books()

        except ValueError:
            print("Invalid input! Please enter a numeric book ID.")

    elif choice == "2":
        library.display_available_books()

    elif choice == "3":
        try:
            book_id = int(input("Enter book ID to search: "))
            library.search_book(book_id)

        except ValueError:
            print("Invalid input! Please enter a numeric book ID.")

    elif choice == "4":
        try:
            book_id = int(input("Enter book ID to issue: "))
            library.issue_book(book_id)
            library.save_books()

        except ValueError:
            print("Invalid input! Please enter a numeric book ID.")

    elif choice == "5":
        try:
            book_id = int(input("Enter book ID to return: "))
            library.return_book(book_id)
            library.save_books()

        except ValueError:
            print("Invalid input! Please enter a numeric book ID.")

    elif choice == "6":
        library.save_books()
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
