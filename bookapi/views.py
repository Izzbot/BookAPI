from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bookapi.models import Books
from bookapi.serializers import BooksSerializer

@api_view(['GET', 'POST'])
def book_list(request, format=None):
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def book_detail(request, pk, format=None):
    try:
        book = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BooksSerializer(book)
        return Response(serializer.data)
