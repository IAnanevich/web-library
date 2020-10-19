from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from book.serializers import BookSerializer, BookDetailSerializer, BookCreateSerializer
from book.models import Book


class BookDetailView(viewsets.ViewSet):
    def detail_book(self, request, pk=None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BookDetailSerializer(user)
        return Response({f"book {pk}": serializer.data})


class BookView(viewsets.ViewSet):
    def post(self, request):
        book = request.data.get('books')
        serializer = BookCreateSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"success": f"Article {book_saved.title} created successfully"})

    def list_books(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response({"books": serializer.data})