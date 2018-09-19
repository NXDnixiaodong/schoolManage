
from django.conf.urls import url

from recordApp import views

app_name = 'record'

urlpatterns = [
    url(r'^member_list/$', views.member_list),
    url(r'^member_edit/$', views.member_edit),
    url(r'^member_add/$', views.member_add),
    url(r'^member_list_rec/$', views.member_list_rec),
    url(r'^search_stu/$', views.search_stu),
    url(r'^search_rec_stu/$', views.search_rec_stu),
    url(r'^ajax_status/$', views.ajax_status),
    url(r'^ajax_del/$', views.ajax_delete),
    url(r'^ajax_rec/$', views.ajax_rec),
    url(r'^ajax_rec_all/$', views.ajax_rec_all),
    url(r'^ajax_del_all/$', views.ajax_del_all),
    url(r'^ajax_stu_edit/$', views.ajax_stu_edit),
    url(r'^ajax_stu_add/$', views.ajax_stu_add),
]
