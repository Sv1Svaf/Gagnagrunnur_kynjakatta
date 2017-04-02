from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(heim|index)*$', views.index, name='index'),
    url(r'^leita/*.*', views.search, name='search'),
	url(r'^kettir/.*',views.catview, name='catview'),
    url(r'^leit/.*', views.findcat, name='findcat'),
    url(r'^kettir$', views.kitty, name='kitty'),
] 
