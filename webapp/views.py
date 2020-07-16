from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import AccessRecord, Topic, Webpage


def index(request):
    webpagesList = AccessRecord.objects.order_by('date')
    
    dictionary = {
        'accessRecords': webpagesList,
        'title': 'Hello, Im a title coming from webapp/views.py!'
    }

    return render(request,  'webapp/home.html', context=dictionary)
