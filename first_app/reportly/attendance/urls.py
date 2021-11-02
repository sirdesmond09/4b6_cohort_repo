from django.urls import path
from .views import test_view

app_name = 'attendance'

urlpatterns = [
    path("books/", test_view, name='all_books')
]
