# -*- coding: utf-8 -*-
"""gis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from drtm.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url( r'^GetData/$', get_data_quest),
    url( r'^login/$', login),
    url( r'^logout/$', logout),
    url( r'^login_validate/$', login_validate),
    url( r'^$', base),
    url( r'^tables/$', tables),
    url( r'^get_build_table_data/$', get_build_table_data),
    url( r'^stables/$', sb_tables),
    url( r'^map/$', map),
    url( r'^build_detal_information/$', build_detal_information),
    url( r'^send_claim/$', send_claim),
    url( r'^test_build/$', test_build),
     url( r'^base/$', base),

]
