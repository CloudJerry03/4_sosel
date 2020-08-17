from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jasoseol(models.Model):
    title = models.CharField(max_length=50)#max_length 필수
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)#자동으로 관리가 됨
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE)