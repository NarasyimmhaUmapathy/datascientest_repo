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
    return library

def test_init():
  
    book = Book(author,title)
    assert book.author == author
    assert book.title == title

def test_add_book(library_init):
    book3 = Book("bbb","ccc")
    library_init.add_book(book3.author,book3.title)
    assert library_init.search_book_author(author).author ==  book3.author

def test_return_books(library_init):
    library_init.add_book(book1.author,book1.title)
    library_init.add_book(book2.author,book2.author)
    
    assert len(library_init.books) == 2

def test_remove_book(library_init):
    library_init.add_book(book1.author,book1.title)
    library_init.remove_book(book1.title)
    assert library_init.search_book_author(book1.author) == None
    

