from django.db import models

# Create your models here.

class Recipe(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    img=models.ImageField(upload_to='recipees')
