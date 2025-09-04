# Query all books by a specific author.
from os import name
from relationship_app.models import Book, Author, Library

author_books = Book.objects.filter(authorn_ame="author_name")


# List all books in a library.
library_books = Library.objects.get(name="library_name").books.all()


# Retrieve the librarian for a library.
librarian = Library.objects.get(name="library_name").librarian