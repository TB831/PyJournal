from django.conf.urls import url
#Basic login module provided by Django
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url('^login/$', login, {'template_name':'login.html'}, name='login'),
]