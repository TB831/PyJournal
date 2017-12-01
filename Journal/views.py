# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.
#Views define/create the logic for the websites
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
            form.save()
            return HttpResponseRedirect(reverse('Journal:topics'))
    context = {'form': form}
    return render(request, 'new_topic.html', context)

def new_entry(request, topic_id):
    #Adds the entry for the specific topic
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('Journal:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)