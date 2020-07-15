from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    myDictionary = {
        'subtitle': 'Hello, Im a subtitle coming from webapp/views.py!'
    }
    return render(request,  'webapp/home.html', context=myDictionary)
