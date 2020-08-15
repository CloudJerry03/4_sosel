from django.db import models

# Create your models here.
class Jasoseol(models.Model):
    title = models.CharField(max_length=50)#max_length 필수
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)#자동으로 관리가 됨