#coding=utf-8
from django.conf.urls import url
from . import views
from staffApp import views


app_name = 'staff'
urlpatterns = [
    url(r'^staffadd/',views.staff_view),
    url(r'^stafflist/',views.stafflist_view),
    url(r'^staffpage/(\d+)',views.stafflist_view),
    url(r'^staffsearch/',views.staffsearch_view),
    url(r'^staffupdate/(\d+)',views.staffupdate_view),
    url(r'^staffupdated/(\d+)',views.staffupdated_view),
    url(r'^$', views.index, name='index'),
    url(r'find/', views.find, name='find'),
    url(r'add/', views.add, name='add'),
]
