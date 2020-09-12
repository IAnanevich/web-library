from rest_framework.response import Response
from rest_framework.views import APIView

from book.serializers import BookSerializer, BookDetailSerializer, BookCreateSerializer
from book.models import Book


class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)


class BookCreateView(APIView):
    def post(self, request):
        book = request.data.get('books')
        serializer = BookCreateSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"success": f"Article {book_saved.title} created successfully"})

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
