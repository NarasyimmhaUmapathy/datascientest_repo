import pytest
from books import Book,Library

author = "aaa"
title = "bbb"
book1 = Book(author,title)
book2 = Book(author,title)
books = [book1,book2]

@pytest.fixture
def library_init():
    library = Library()

def test_init():
  
    book = Book(author,title)
    assert book.author == author
    assert book.title == title

def test_add_book(library_init):
    library_init.add_book(books)
    assert len(library_init.books) == 2

def test_return_books(library_init):
    
    books = [book1,book2]
    library_init.add_book(books)
    assert len(library_init.books) == 2

def test_remove_books(library_init):
    library_init.add_book(books)
    library_init.remove_book(books)
    assert len(library_init.books) == 0
