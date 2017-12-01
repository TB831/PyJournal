# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def topics(request):
    #Shows different topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    #Shows a single topic and its entries
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries': entries}
    return render(request, 'topic.html', context)

def new_topic(request):
    #Adds a new topic
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save
            return HttpResponseRedirect(reverse('Journal:topics'))
    context = {'form': form}
    return render(request, 'new_topic.html', context)