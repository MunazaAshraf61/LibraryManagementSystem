# Library Management System

## About the Project

This is a simple Library Management System developed using Python. It helps manage books in a library by allowing users to add books, view available books, search for books, issue books, and return them.

The project uses object-oriented programming concepts and a CSV file to store book information so that the data can be loaded again when the program is reopened.

## Features

- Add new books to the library.
- Display all available books.
- Search for a book using its ID.
- Issue a book.
- Return an issued book.
- Save book information in a CSV file.
- Load previously saved book information when the program starts.
- Handle invalid inputs and basic file errors.

## Technologies Used

- **Python 3**
- **CSV module** for storing book records
- **Object-Oriented Programming (OOP)**

## Concepts Used

- Classes and objects
- Inheritance
- Abstraction
- Methods and constructors
- File handling
- Exception handling
- Lists and loops

## Files in the Project

- `library_management.py` – contains the Python code for the project.
- `books.csv` – stores book details and their availability status.
- `output.png` – screenshot showing the program running.
- `README.md` – provides information about the project.

*Note: Use your actual Python filename and screenshot filename if they are different.*

## How to Run the Project

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in your terminal or command prompt.
4. Run the following command:

   ```bash
   python library_management.py
   ```

5. Follow the menu displayed on the screen to perform different operations.

## How Data Is Stored

Book details are saved in `books.csv`. When the program starts, it loads the previously saved records. This allows book information and availability status to remain saved between program sessions.

## Limitations

This is a basic project created for learning Python. It currently focuses on managing books and their availability. Student records and information about which student has borrowed a particular book are not fully connected to the menu system.

## Conclusion

Building this project helped me practise Python programming, object-oriented programming, CSV file handling, and exception handling while creating a basic library management system.