import signal
import sys


def signal_handler(sig, frame):
    print('\n\nNow exiting gracefully, goodbye!\n')
    sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)


class Bookshelf:
    def __init__(self, category, username):
        self.books = {}
        self.category = category
        self.username = username

    def addBook(self):
        prYellow("""\n------------------------
You are now adding a book:
-------------------------\n""")
        book = {
            "copies": {
                "copiesTaken": 0
            }
        }
        book["name"] = input("Name of the book: ")
        book["author"] = input("\nName of the author: ")
        book["copies"]["totalCopies"] = input("\nCopies of the book: ")

        self.book[book["name"].lower()] = book

        prCyan(
            f'\nBook {book["name"]} by {book["author"]} added. ({book["copies"]["totalCopies"]} Copies)')

    def removeBook(self):
        removeName = input("Name of the book to remove: ").lower()
        if self.books.get(removeName, False):
            self.books.remove(removeName)
            prCyan("Book removed from bookshelf!")
        else:
            prCyan("Book not found in bookshelf.")

    def checkoutBook(self):
        pass

    def listBooks(self):
        pass


def prYellow(skk): print("\033[93m{}\033[00m".format(skk))
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk))


prYellow("""----------------------------------------------------------
Welcome to bookworm! Please type needed information below:
----------------------------------------------------------""")
user = input("Name: ")
bookshelf_category = input("\nCategory of Bookshelf: ")
print("\nA {} Bookshelf has been created by {}.".format(bookshelf_category, user))
bookshelf = Bookshelf(bookshelf_category, user)
while True:
    prYellow("""
    Actions that can be performed are:
    - Add book (a)
    - Remove book (r)
    - Checkout book (c)
    - List books (l)
    - Exit (Control + C)
    """)
    action = input("Action (a/r/c/l): ").lower()

    actionList = {
        "a": bookshelf.addBook,
        "r": bookshelf.removeBook,
        "c": bookshelf.checkoutBook,
        "l": bookshelf.listBooks
    }
    if actionList.get(action, False):
        actionList.get(action)()
