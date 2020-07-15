from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    dictionary = {
        'title': 'Hello, Im a title coming from webapp/views.py!'
    }
    return render(request,  'webapp/home.html', context=dictionary)
