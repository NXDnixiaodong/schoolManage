from django.conf.urls import url
from staffApp import views


app_name = 'staff'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'find/', views.find, name='find'),
    url(r'add/', views.add, name='add'),
]
