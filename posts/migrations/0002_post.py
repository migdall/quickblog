# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='uploads/images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Person')),
            ],
        ),
    ]