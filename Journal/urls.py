from django.conf.urls import url

from . import views

urlpatterns = [
    #Index
    url(r'^$', views.index, name='index'),

    #Topics
    url(r'^topics/$', views.topics, name='topics'),

    #Details for single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #Page to add a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]