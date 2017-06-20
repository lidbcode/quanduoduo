from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.


def index(request):
    items = models.ItemsInfo.objects.all()
    return render(request, 'dwxk/index.html', {'items': items})


def test(requset):
    return HttpResponse("welcome to test")
