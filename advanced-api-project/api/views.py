from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.

# For retrieving all books.
class ListView(ListAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializer

# For retrieving a single book by ID.
class DetailView(RetrieveAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializer

# For adding a new book.
class CreateView(CreateAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializer

# For modifying an existing book.
class UpdateView(UpdateAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializer

# For removing a book.
class DeleteView(DestroyAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializer