# Library Management System

A command-line library management system built in Python, demonstrating Object-Oriented Programming (OOP) concepts such as classes, inheritance, and polymorphism.

## Features

- Add, remove, update, and display books (physical books, e-books, and audiobooks)
- Add, remove, update, and display library members
- Issue and return books
- Automatic member ID assignment
- ISBN duplicate prevention
- Password-protected administrator menu

## Project Structure

```
Library Management System/
│
├── book.py          # Book, Ebook, and Audiobook classes
├── member.py        # Member class
├── library.py       # Library class
├── main.py          # Command-line interface
├── test_library.py  # Unit tests
└── README.md
```

## OOP Concepts Demonstrated

**Classes and Objects** – The system is built around four classes: `Book`, `Member`, `Library`, and subclasses `Ebook` and `Audiobook`.

**Inheritance** – `Ebook` and `Audiobook` both inherit from `Book`, reusing shared attributes like `title`, `author`, `isbn`, and `copies`.

**Polymorphism** – Each book type overrides the `display_info()` method, displaying type-specific information while being called the same way.

## How to Run

Make sure you have Python 3 installed, then navigate to the project folder and run:

```bash
python3 main.py
```

## Usage

The system has two menus:

**Låner menu (Member menu)**
- Borrow a book by title or ISBN
- Return a borrowed book

**Administrator menu** (password: 1234)
- Add, remove, and update books
- Add, remove, and update members
- Display all books and members

## Requirements

- Python 3.x
- No external libraries required
