# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.


def index(request):
    items = models.ItemsInfo.objects.filter(c1 == -5)
    category = [{'c1': '-1', 'name': '女装'},
                {'c1': '-2', 'name': '女装'},
                {'c1': '-3', 'name': '女装'},
                {'c1': '-4', 'name': '女装'},
                {'c1': '-5', 'name': '女装'},
                {'c1': '-6', 'name': '女装'},
                {'c1': '-7', 'name': '女装'},
                {'c1': '-8', 'name': '女装'},
                {'c1': '-9', 'name': '女装'},
                {'c1': '-10', 'name': '女装'}
                ]
    return render(request, 'dwxk/index.html', {'items': items, 'category': category})


def test(requset):
    return HttpResponse("welcome to test")
