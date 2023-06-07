from django.db import models

# Create your models here.

class Employees(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=180)
    major=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    age=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    
    