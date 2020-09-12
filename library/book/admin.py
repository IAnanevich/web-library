from django.contrib import admin
from book.models import Author, Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "author_name")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
