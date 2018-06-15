from django.conf.urls import url

from . import views

app_name = 'mainsite'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^people/$', views.people, name='people'),
    url(r'^events/$', views.events, name='events'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^live/$', views.live, name='live'),
]