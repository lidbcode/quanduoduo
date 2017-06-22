# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.


def index(request):
    items = models.ItemsInfo.objects.filter(c1=-5)
    category = [{'cid': '-1', 'cname': '女装'},
                {'cid': '-2', 'cname': '女装'},
                {'cid': '-3', 'cname': '女装'},
                {'cid': '-4', 'cname': '女装'},
                {'cid': '-5', 'cname': '女装'},
                {'cid': '-6', 'cname': '女装'},
                {'cid': '-7', 'cname': '女装'},
                {'cid': '-8', 'cname': '女装'},
                {'cid': '-9', 'cname': '女装'},
                {'cid': '-10', 'cname': '女装'}
                ]
    return render(request, 'dwxk/index.html', {'items': items, 'category': category})


def get_category(request, cid, cname):
    items = models.ItemsInfo.objects.filter(c1=cid)
    return render(request, 'dwxk/category.html', {'cid': cid, 'cname': cname})


def test(requset):
    return HttpResponse("welcome to test")
