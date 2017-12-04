# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#Import for Django based logout module
from django.contrib.auth import logout

# Create your views here.
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Journal:index'))