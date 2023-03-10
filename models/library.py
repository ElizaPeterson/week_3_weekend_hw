from models.book import *

book1 = Book("Dune", "Frank Herbert", "Sci-fi", False)
book2 = Book("Lord of the Rings: The Fellowship of the Ring", "J. R. R. Tolkien", "Fantasy", True)
book3 = Book("Fantastic Mr. Fox", "Roald Dahl", "Children's Novel", False)

books = [book1, book2, book3]

def add_new_book(new_book):
    books.append(new_book)

def remove_book(index):
    books.remove(books[int(index-1)])

def check_in(index):
    books[int(index-1)].checked_out == True

def check_out(index):
    books[int(index-1)].checked_out == False
