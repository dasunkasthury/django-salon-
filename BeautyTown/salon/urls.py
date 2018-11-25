from django.urls import path, include , re_path
from . import views

app_name = 'salon'

urlpatterns = [
  # /movies/
  re_path(r'^$',views.index,name = 'index'),

  # /movies/785/
  #re_path(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),

  # /movies/785/favourite/
  #re_path(r'^(?P<movie_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),

]