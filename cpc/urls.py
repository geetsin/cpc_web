from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^contact/', views.contact, name="contact"),
    url(r'^home/$', views.index, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^events/$', views.events, name='events'),
]
