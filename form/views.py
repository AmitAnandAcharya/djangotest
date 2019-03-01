# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
from subprocess import call

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            hostname = form.cleaned_data.get('your_name')
            call("echo " + hostname + " > file1", shell = True)
            call('ansible-playbook /django/portal/form/hostname.yml' ,shell=True)
            package = form.cleaned_data['your_package']
            call("echo " + package + " > file2", shell = True)
	    call('ansible-playbook /django/portal/form/install.yml' ,shell=True)
	    context = {"hostname":hostname, "package":package}
            return render(request, 'name.html', context)
          

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
