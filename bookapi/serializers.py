from django.forms import widgets
from rest_framework import serializers
from bookapi.models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'authors', 'pub_date', 'publisher', 'summary', 'price', 'book_url', 'cover_url')

    def create(selfself, validated_data):
        return Books.objects.create(**validated_data)
