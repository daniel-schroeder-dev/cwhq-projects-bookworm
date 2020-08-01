from book import *
from bookshelf import *


if __name__ == "__main__":
    
    name = input("What is your name? ")
    bookshelf = Bookshelf(input("What category of bookself do you want to use? "), name)

    def one_or_more(number, first, second):
        
        return first if len(bookshelf.books) == number else second


    while True:
        add = input(f"Would you like to add {one_or_more(0, 'a book', 'more books')}? (Y/N) ")
        if add.lower() == "y":
            title = input("What is the books title? ")
            author = input("What is the books author? ")
            book = Book(title, author)
            bookshelf.addBook(book)
        else:
            break

    print("\nThe following {} are in {}'s {} bookshelf:\n".format(one_or_more(1, 'book', 'books'), bookshelf.owner, bookshelf.name))


    for book in bookshelf.books:
        print(book)
