# Query all books by a specific author.
from os import name
from relationship_app.models import Book, Author, Library

author_books = Book.objects.filter(author_name="author_name")


# List all books in a library.
Library.objects.get(name=library_name).books.all()
# library_books = Library.objects.get(name="library_name").books.all()


# Retrieve the librarian for a library.
librarian = Library.objects.get(name="library_name").librarian