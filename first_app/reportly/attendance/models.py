from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    cohort = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
        
class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default=10)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="books")
    body = models.TextField()
    isbn = models.CharField(max_length=42, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title



# Book.objects.or