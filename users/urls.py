from django.conf.urls import url
#Basic login module provided by Django
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #URL config for logging in
    url('^login/$', login, {'template_name':'login.html'}, name='login'),
    #URL config for logging out
    url(r'^logout/$', views.logout_view, name='logout'),
    #URL config for registration
    url(r'^register/', views.register, name='register'),
]