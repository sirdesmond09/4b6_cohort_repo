from django.contrib import admin
from .models import Book, Student

# Register your models here.
admin.site.register(Student)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'id','no_of_pages', 'isbn', 'date']
    list_editable = ['isbn']
    list_filter = ['date']
    list_per_page = 10
    search_fields = ['title', 'body', 'author']