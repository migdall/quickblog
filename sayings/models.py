import uuid
from django.db import models

# Create your models here.


class Question(models.Model):
    content = models.CharField(max_length=255)


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recording_url = models.URLField(max_length=255)
    question = models.ForeignKey(Question)


class Hero(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    polly_language_code = models.CharField(max_length=30)
    polly_voice_id = models.CharField(max_length=30)


class Saying(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(auto_now=True)
    hero = models.ForeignKey(Hero, null=True, blank=True)
    answers = models.ManyToManyField(Answer, blank=True)

