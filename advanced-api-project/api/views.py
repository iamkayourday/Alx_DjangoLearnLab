from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.

# For retrieving all books.
class ListView(ListAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# For retrieving a single book by ID.
class DetailView(RetrieveAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# For adding a new book.
class CreateView(CreateAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# For modifying an existing book.
class UpdateView(UpdateAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# For removing a book.
class DeleteView(DestroyAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]