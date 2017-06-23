# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.


def index(request):
    items = models.ItemsInfo.objects.order_by("-sales_num")[0:50]
    category = [{'cid': '-1', 'cname': '女装'},
                {'cid': '-2', 'cname': '箱包'},
                {'cid': '-3', 'cname': '配饰'},
                {'cid': '-4', 'cname': '美妆个护'},
                {'cid': '-5', 'cname': '食品'},
                {'cid': '-6', 'cname': '家居百货'},
                {'cid': '-8', 'cname': '母婴'},
                {'cid': '-9', 'cname': '手机数码'},
                {'cid': '-12', 'cname': '鞋靴'},
                {'cid': '-13', 'cname': '男装'}
                ]
    return render(request, 'dwxk/index.html', {'items': items, 'category': category})


def get_category(request, cid, cname):
    items = models.ItemsInfo.objects.filter(c1=cid)
    return render(request, 'dwxk/category.html', {'items': items, 'cname': cname})


def get_search(request):
    keyword = request.GET['keyword']
    items = models.ItemsInfo.objects.filter(ad_name__contains=keyword)
    return render(request, 'dwxk/search.html', {'items': items, 'keyword': keyword})


def test(requset):
    return HttpResponse("welcome to test")
