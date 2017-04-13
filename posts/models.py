from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    editor = models.BooleanField(default=False)

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.FileField(upload_to='uploads/images/')
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

