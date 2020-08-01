class Bookshelf:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.books = []

    def addBook(self, book):
        self.books.append(book)
