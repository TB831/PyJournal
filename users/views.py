# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#Import from Django based logout module
from django.contrib.auth import logout, login, authenticate
#Import from Django module that creates a user with given username and password
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Journal:index'))

def register(request):
    if request.method !='POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            auth_user = authenticate(username=new_user.username,
                                     password=request.POST['password1'])
            login(request,auth_user)
            return HttpResponseRedirect(reverse('Journal:index'))

    context = {'form':form}
    return render(request, 'register.html', context)