# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Topic(models.Model):
    #adds a topic
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    #adds a text entry
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    image = models.FileField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        #return string representation of the model
        return self.text[:50] + "..."