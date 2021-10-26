from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'no_of_pages', 'isbn', 'date']
    list_editable = ['isbn']
    list_filter = ['date']
    list_per_page = 2
    search_fields = ['title', 'body', 'author']