from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("author", "publication_year")
# Register your models here.
admin.site.register(Book, BookAdmin)
