from django.conf.urls import url
from .views import new_saying, set_hero

urlpatterns = [
    url(r'^saying/add/$', new_saying, name='create a new saying'),
    url(r'^(?P<saying_id>[\W\w]+)/hero/$', set_hero, name='pick a hero for your saying')
]
