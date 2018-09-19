# -*- coding: utf-8 -*-
from django.conf.urls import url
from scoreApp import views


app_name = 'score'
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^delete/',views.delete, name='delete'),
    url(r'^add/',views.add, name='add'),
    url(r'^add(\d+)',views.add_ajax, name='add_ajax'),
    url(r'^find',views.find, name='find'),
    # url(r'^grade/',views.grade, name='grade'),
    url(r'^clazz/',views.clazz, name='clazz'),
]
