from django.forms import widgets
from rest_framework import serializers
from bookapi.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'authors', 'pub_date', 'publisher', 'summary', 'price', 'book_url', 'cover_url')

    def create(selfself, validated_data):
        return Books.objects.create(**validated_data)
