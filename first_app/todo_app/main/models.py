from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_do')
    activity = models.CharField(max_length=350)
    completed =  models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'{self.activity} for {self.user.username}'