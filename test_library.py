import unittest
from book import Book, Audiobook, Ebook
from member import Member
from library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book = Book("1984", "George Orwell", "123", 5)
        self.member = Member("Test_Dummy")

    def test_add_book(self):
        """Tester om en bog kan tilføjes til systemet"""
        self.library.add_book(self.book)
        self.assertIn(self.book, self.library.books)

    def test_duplicate_isbn(self):
        """Tilføjer en bog, og prøver så at tilføje den samme bog igen for at se om den afviser duplikater"""
        self.library.add_book(self.book)
        self.library.add_book(self.book)
        self.assertEqual(len(self.library.books), 1)

    def test_borrow_book(self):
        """Tester om en bog kan tilføjes til en låner, og om antal kopier går ned med en"""
        self.library.add_book(self.book)
        self.library.add_member(self.member)
        self.member.borrow_book(self.book)
        self.assertEqual(self.book.copies, 4)
        self.assertIn(self.book, self.member.borrowed_books)
    
    def test_return_book(self):
        """Tester om en bog kan afleveres"""
        self.library.add_book(self.book)
        self.library.add_member(self.member)
        self.member.borrow_book(self.book)
        self.member.return_book(self.book)
        self.assertEqual(self.book.copies, 5)
        self.assertNotIn(self.book, self.member.borrowed_books)

    def test_borrow_unavailable_book(self):
        """Tester at man ikke kan låne en bog der allerede er udlånt"""
        self.book.copies = 0
        self.library.add_book(self.book)
        self.library.add_member(self.member)
        self.member.borrow_book(self.book)
        self.assertNotIn(self.book, self.member.borrowed_books)

    def test_return_unborrowed_book(self):
        """Tester at man ikke kan returnere en bog der ikke er lånt"""
        self.library.add_book(self.book)
        self.library.add_member(self.member)
        self.member.return_book(self.book)
        self.assertTrue(self.book.copies, 5)
