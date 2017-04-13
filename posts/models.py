from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    editor = models.BooleanField(default=False)

