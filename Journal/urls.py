from django.conf.urls import url

from . import views

urlpatterns = [
    #Index
    url(r'^$', views.index, name='index'),
]