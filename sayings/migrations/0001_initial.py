# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-18 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('recording_url', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
                ('polly_language_code', models.CharField(max_length=30)),
                ('polly_voice_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Saying',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.DateTimeField(auto_now=True)),
                ('answers', models.ManyToManyField(to='sayings.Answer')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sayings.Hero')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sayings.Question'),
        ),
    ]
