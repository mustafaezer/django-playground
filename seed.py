
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from faker import Faker
from webapp.models import AccessRecord, Topic, Webpage
import random

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def addTopic():
    t = Topic.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = addTopic()

        fakeUrl = fakegen.url()
        fakeDate = fakegen.date()
        fakeName = fakegen.company()

        webpage = Webpage.objects.get_or_create(
            topic=top, url=fakeUrl, name=fakeName)[0]
        accessRecord = AccessRecord.objects.get_or_create(
            name=webpage, date=fakeDate)[0]

if __name__ == '__main__':
    print("Populating script...")
    populate(20)
    print("Populating complete!")
