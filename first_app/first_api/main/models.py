from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
def get_cohort():
    date=timezone.now()
    cohort = datetime.strftime(date, "%B-%Y")
    return cohort
    

class Student(models.Model):
    name=models.CharField(max_length=20)
    cohort=models.CharField(max_length=25, default=get_cohort())
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def book(self):
        return self.books.all().values()
    
    
    
    
    
    
class Book(models.Model):
    title=models.CharField(max_length=25)
    author=models.CharField(max_length=20)
    no_of_pages=models.IntegerField()
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='books')
    body=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  
    
    @property
    def student_name(self):
        return self.student.name
    
