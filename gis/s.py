# -*- coding: utf-8 -*-
"""
Django settings for gis project.

Generated by 'django-admin startproject' using Django 1.9.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from os.path import abspath, join, dirname

import django.template.context_processors
import django.contrib.auth.context_processors
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = (join(BASE_DIR, 'static'),)

print(BASE_DIR,STATICFILES_DIRS)