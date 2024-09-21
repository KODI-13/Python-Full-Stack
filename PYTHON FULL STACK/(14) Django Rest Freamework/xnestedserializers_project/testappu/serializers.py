from testappu.models import Author, Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books_by_author = BookSerializer(read_only=True, many=True)     # 1st param(read_only=True) = books information is in only read mode cant modify it .... 2nd param(many=True) = beacuse each author can have many books
    class Meta:
        model = Author
        fields = '__all__'