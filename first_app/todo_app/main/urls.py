from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo),
    path('todos/<int:todo_id>', views.todo_detail),
]