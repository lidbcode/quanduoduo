# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core import serializers
import json
from itertools import chain

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
    items = models.ItemsInfo.objects.order_by("-sales_num").filter(c1=cid)
    return render(request, 'dwxk/category.html', {'items': items, 'cname': cname})


def get_search(request):
    keyword = request.GET['keyword']
    items = models.ItemsInfo.objects.order_by("-sales_num").filter(ad_name__contains=keyword)
    return render(request, 'dwxk/search.html', {'items': items, 'keyword': keyword})


def test(requset):
    return HttpResponse("welcome to test code is delete ")


## api


def get_banner_info(request):
    banner = models.BannerInfo.objects.all()
    return HttpResponse(serializers.serialize("json", banner))


def get_brand_info(request):
    brand = models.BrandInfo.objects.order_by("brand_id")
    return HttpResponse(serializers.serialize("json", brand))


def get_brand_items(request,brand_id,page):
    start = 10 * (int(page) - 1)
    end = start + 10
    items = []
    if(int(brand_id) == 0 ):
        items = models.ItemsInfo.objects.exclude(brand_id = 0).order_by("-sales_num")[start:end]
    else:
        items = models.ItemsInfo.objects.filter(brand_id = brand_id).order_by("-sales_num")[start:end]
    return HttpResponse(serializers.serialize("json", items))


def get_category_info(request):
    base_url = "../common/image/"
    category = [{'cid': '-1', 'cname': '女装','img_url': base_url+'c-1.png'},
                {'cid': '-2', 'cname': '箱包','img_url': base_url+'c-2.png'},
                {'cid': '-3', 'cname': '配饰','img_url': base_url+'c-3.png'},
                {'cid': '-4', 'cname': '美妆个护','img_url': base_url+'c-4.png'},
                {'cid': '-5', 'cname': '食品','img_url': base_url+'c-5.png'},
                {'cid': '-6', 'cname': '家居百货','img_url': base_url+'c-6.png'},
                {'cid': '-8', 'cname': '母婴','img_url': base_url+'c-8.png'},
                {'cid': '-9', 'cname': '手机数码','img_url': base_url+'c-9.png'},
                {'cid': '-12', 'cname': '鞋靴','img_url': base_url+'c-12.png'},
                {'cid': '-13', 'cname': '男装','img_url': base_url+'c-13.png'}
                ]
    return HttpResponse(json.dumps(category))


def get_category_items(request,cid,page):
    start = 10 * (int(page) - 1)
    end = start + 10
    items = []
    if(int(cid) == 0 ):
        items = models.CategoryItems.objects.order_by("-sales_num")[start:end]
    else:
        items = models.CategoryItems.objects.filter(c1=cid).order_by("-sales_num")[start:end]  
    return HttpResponse(serializers.serialize("json", items))


def get_search_items(request,keyword,page):
    start = 10 * (int(page) - 1)
    end = start + 10
    items = models.BrandItems.objects.filter(ad_name__contains=keyword).order_by("-sales_num")[start:end]
    return HttpResponse(serializers.serialize("json", items))
