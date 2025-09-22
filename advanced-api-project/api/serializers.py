from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer for Author and Book models
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name'
            ]
        

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 
            'title', 
            'publication_year', 
            'author'
            ]
        
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
 

