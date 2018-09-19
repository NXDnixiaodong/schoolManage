# conding=utf-8

from django.conf.urls import url

from libApp import views

app_name = 'lib'
urlpatterns = [
    url(r'^list/$',views.list_view),
    url(r'^list/(\d+)$',views.list_view),
    url(r'^manage/', views.manage_view),
    url(r'^add/', views.add_view),
    url(r'^sreach/', views.sreach_view),
    url(r'^update/(\d+)$', views.update_view),
    url(r'^update/', views.update_view),
    url(r'^update1/(\d+)$', views.update1_view),
    url(r'^delete/', views.delete_view),

]
