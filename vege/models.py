from django.db import models
from django.contrib.auth.models import User #this is a user model


# Create your models here.

class Recipe(models.Model):
    user=models.ForeignKey(User , on_delete=models.SET_NULL, null=True, blank=True)
    name=models.CharField(max_length=30)
    desc=models.TextField()
    img=models.ImageField(upload_to='recipees')
