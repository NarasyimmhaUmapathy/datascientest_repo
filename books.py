class Book():
    def __init__(self,author,title):
        self.author=author
        self.title=title

class Library():
    def __init__(self,books):
        self.books = []

    def add_book(self,books):
        
        [self.books.append(i) for i in books]
    
    def remove_book(self,author,title):
        book = [b for b in self.books if b.title == title]
        self.books.remove(book)

    def list_books(self,author,title):
        return self.books
    
    def search_book_author(self,author,title):
        book = [b for b in self.books if b.author == author]
        return book
    