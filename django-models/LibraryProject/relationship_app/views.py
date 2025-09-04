from django.shortcuts import render
from django.views.generic import DetailView
from .models import *


# Create your views here.

# Function-based View to display list of books
def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'list_books.html', context)

# Class-based view that displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'