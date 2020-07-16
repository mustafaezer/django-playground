from __future__ import unicode_literals
from django.contrib import admin
from webapp.models import AccessRecord, Topic, Webpage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
