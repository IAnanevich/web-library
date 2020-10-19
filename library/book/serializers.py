from rest_framework import serializers
from book.models import Book


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author_name')

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author_name')


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author_name_id')
