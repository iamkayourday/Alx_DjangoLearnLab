from django.shortcuts import render
# from django.views.generic import DetailView
from .models import Library, Book
# from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.

# Function-based View to display list of books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view that displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Register view
class RegisterView(CreateView):
    form_class = UserCreationForm
    # If this is a function based view it would be 
    # form = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

