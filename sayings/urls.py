from django.conf.urls import url
from .views import new_saying, set_hero, get_question

urlpatterns = [
    url(r'^saying/add/$', new_saying, name='create a new saying'),
    url(r'^(?P<saying_id>[\W\w]+)/hero/$', set_hero, name='pick a hero for your saying'),
    url(r'^(?P<saying_id>[\W\w]+)/questions/(?P<question_id>[\d]+)/$', get_question, name='the first question')
]
