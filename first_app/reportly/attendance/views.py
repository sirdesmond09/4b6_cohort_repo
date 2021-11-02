from django.shortcuts import render
from .models import Book

# Create your views here.


def test_view(request):
    my_books = Book.objects.all()
    # print(my_books)
    data = {
        'books':my_books
    }
    return render(request, 'test.html',data)
