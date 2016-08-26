from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<character_id>[0-9]+)/$', views.character, name='character'),
    url(r'^search/', views.search, name='search'),
    url(r'^add_from_swapi/(?P<character_id>[0-9]+)/$', views.add_from_swapi, name='add_from_swapi'),
    url(r'^request_log/', views.request_log, name='request_log'),
    url(r'^add/', views.add, name='add'),
    url(r'^edit/(?P<character_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<character_id>[0-9]+)/$', views.delete, name='delete'),

]