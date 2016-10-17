# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Question, Choice, Build, Balans, Service, Street

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Build)
admin.site.register(Balans)
admin.site.register(Service)
admin.site.register(Street)
