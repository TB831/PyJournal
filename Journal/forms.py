from django import forms
from .models import Topic

class TopicForm():
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}