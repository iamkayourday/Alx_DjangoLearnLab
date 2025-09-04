# Query all books by a specific author.
from os import name
from relationship_app.models import Book, Author, Library

author_books = Book.objects.filter(author_name="Author Name")


# List all books in a library.
library_books = Library.objects.get(name="Library Name").books.all()


# Retrieve the librarian for a library.
librarian = Library.objects.get(name="Library Name").librarian