from django.contrib import admin
from .models import Question, Answer, Hero, Saying

# Register your models here.


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Hero)
admin.site.register(Saying)

