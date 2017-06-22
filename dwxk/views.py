from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.


def index(request):
    items = models.ItemsInfo.objects.all()
    cname = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    return render(request, 'dwxk/index.html', {'items': items, 'cname': cname})


def test(requset):
    return HttpResponse("welcome to test")
