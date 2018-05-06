from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^contact/', views.contact, name="contact"),
    url(r'^home/$', views.index, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^events/$', views.events, name='events'),
    url(r'^login/$', views.login, name='login'),
    url(r'^auth/$', views.auth_views, name='auth_views'),
    url(r'^userPage/$', views.userPage, name='userPage'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^invalidLogin/$', views.invalidLogin, name='invalidLogin'),
]
