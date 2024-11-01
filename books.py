class Book():
    def __init__(self,author,title):
        self.author=author
        self.title=title

class Library():
    def __init__(self,books=None):
        self.books = books

    def add_book(self,author,title):
        book = Book(author,title)
        self.books.append(book)


    def remove_book(self,title):
        book = [b for b in self.books if b.title == title]
        self.books.remove(book)

    def list_books(self):
        return self.books
    
    def search_book_author(self,author):
        book = [b for b in self.books if b.author == author]
        return book
    
