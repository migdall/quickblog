from django.contrib import admin
from django.contrib.auth.models import User

from .models import Person, Post

# Register your models here.

class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'people'

# Register

admin.site.register(Person)
admin.site.register(Post)

