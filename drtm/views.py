# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import  render
from models import Question, Choice, Build
from django.http import JsonResponse,HttpResponseRedirect,Http404,HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core import serializers
import json

login_url='/login/'

@login_required(login_url=login_url)
def get_data_quest(request):
    data = Build.objects.all()[:170]
    requestData=[]
    for i in request.META:
        requestData.append([i,request.META[i]])
    return render(request,r'grid/GridJQuery/index.htm',{'data': data,
                            'requestData':requestData})


@login_required(login_url=login_url)
def sb_admin(request):
    data = Build.objects.all()[:170]
    return render(request,r'grid/Bootstrap/index.html')

@login_required(login_url=login_url)
def sb_tables(request):
    return render(request,r'grid/Bootstrap/tables.html')

@login_required(login_url=login_url)
def map(request):
    return render(request,r'v1/map-element.html',{'Dashboard':'',
    'info':'Карта присутності провадерів інтернет','map':True})

@login_required(login_url=login_url)
def build_detal_information(request):
    id=int(request.GET['id'])
    data = Build.objects.get(id=id)
    adress=str(data)
    balans=str(data.balans)
    service=str(data.service)

    return JsonResponse({'adress':adress,'balans':balans,'service':service})


@login_required(login_url=login_url)
@csrf_exempt # декоратор вимикає перевірку csrf -токена !!!!!!!!!!!!
def send_claim(request):
    id=int(request.POST['id'])
    data = Build.objects.get(id=id)
    adress=str(data)
    balans=str(data.balans)
    service=str(data.service)
    return JsonResponse({'adress':adress,'balans':balans,'service':service})

@login_required(login_url=login_url)
def test_build(request):
    data = Build.objects.all()[1:2].values_list()
    requestData=[]
    for i in data:
        requestData.append(i)
    return render(request,r'map/Object_detal_information.html',{'requestData':requestData})


def login(request):
    return render(request,r'v1/login-form.html')

@login_required(login_url=login_url)
def base(request):
    return render(request,r'v1/base.html')

def tables(request):
    return render(request,r'v1/table.html')


##@csrf_exempt # декоратор вимикає перевірку csrf -токена !!!!!!!!!!!!
def login_validate(request):
     html = "<html><body>Ніхуя не вийшло </body></html>"
     if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Пароль правилен и пользователь “активный”
            auth.login(request, user)
            # Переадресовать на страницу успешного входа.
            return HttpResponseRedirect('../')
        else:
            # Переадресовать на страницу ошибок
            return HttpResponse(html)
     else:
         # Переадресовать на страницу ошибок
         return HttpResponse(html)

def logout(request):
    auth.logout(request)
    # Переадресовать на страницу успешного выхода.
    return HttpResponseRedirect("/login/")

@login_required(login_url=login_url)
def get_build_table_data(request):
    data = Build.objects.all()[:1000]
    jasonDatalist=[]
    for i in data:
        jasonDatalist.append([str(i),str(i.balans),str(i.service)])
    r=json.dumps(jasonDatalist)
    return HttpResponse(r, content_type="application/json")


