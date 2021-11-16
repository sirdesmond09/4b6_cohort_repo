from rest_framework import serializers
from .models import Student, Book


class StudentSerializer(serializers.ModelSerializer):
    book = serializers.ReadOnlyField()
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'cohort', 'date_joined', 'book']
        
        
        
class BookSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField()
    
    class Meta:
        model = Book
        fields = ["id", "title" ,"author", "no_of_pages", "student", "student_name","body","created_at"]