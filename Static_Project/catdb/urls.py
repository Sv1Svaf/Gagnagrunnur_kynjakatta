from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(index)*$', views.index, name='index'),
    url(r'^search/.*', views.search, name='search'),
	url(r'^cat/.*',views.catview, name='catview'),
    url(r'^findcat/.*', views.findcat, name='findcat'),
    url(r'^kitty$', views.kitty, name='kitty'),
	url(r'^mmm',views.fourohfour, name = '404')
] 
