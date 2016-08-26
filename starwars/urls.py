from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<character_id>[0-9]+)/$', views.character, name='character'),
    url(r'^search/', views.search, name='search'),
    url(r'^add_from_swapi/(?P<character_id>[0-9]+)/$', views.add_from_swapi, name='add_from_swapi'),
    url(r'^crud/', views.crud, name='crud'),

]