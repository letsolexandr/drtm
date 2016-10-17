# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

@python_2_unicode_compatible
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text

@python_2_unicode_compatible
class Build(models.Model):
    name=models.CharField(max_length=200, verbose_name='Адреса')
    balans=models.ForeignKey('Balans',null=True)
    service=models.ForeignKey('Service',null=True)
    street=models.ForeignKey('Street',null=True)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Balans(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Service(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Street(models.Model):
    name=models.CharField(max_length=100,null=True)
    old_name=models.CharField(max_length=100,null=True)
    name_display=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name_display

@python_2_unicode_compatible
class TypeBuild(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

