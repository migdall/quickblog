# Urls for the posts app

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^create/$', views.create_post, name='create'),
    url(r'^(\d+)/edit/$', views.edit_post, name='edit'),
    url(r'^(\d+)/delete/$', views.delete_post, name='delete')
]
