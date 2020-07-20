from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import AccessRecord, Topic, Webpage
from webapp import forms
from django.utils.translation import gettext as _


def index(request):
    webpagesList = AccessRecord.objects.order_by('date')

    dictionary = {
        'accessRecords': webpagesList,
        'title': _('Hello, lets get started!')
    }

    return render(request,  'webapp/home.html', context=dictionary)


def createTopicForm(request):
    form = forms.CreateTopicForm()

    if request.method == 'POST':
        form = forms.CreateTopicForm(request.POST)
        if form.is_valid():
            print("Name " + form.cleaned_data['name'])
            form.save()

    return render(request, 'webapp/create-topic.html', {'form': form})
