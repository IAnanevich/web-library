from django.urls import path
from book.views import BookDetailView, BookView

urlpatterns = [
    path('books/', BookView.as_view({'get': 'list_books'})),
    path('books/<int:pk>/', BookDetailView.as_view({'get': 'detail_book'})),
]
