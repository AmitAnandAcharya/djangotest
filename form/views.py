# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
import textwrap
from django.views.generic.base import View

# Create your views here.

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            hostname = form.cleaned_data['your_name']
            package = form.cleaned_data['your_package']
            context = {"hostname":hostname, "package":package}
            return render(request, 'name.html', context)
          

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
