from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.


def index(request):
    items = models.ItemsInfo.objects.all()
    category = [{u'c1': u'-1', u'name': u'女装'},
                {u'c1': u'-2', u'name': u'女装'},
                {u'c1': u'-3', u'name': u'女装'},
                {u'c1': u'-4', u'name': u'女装'},
                {u'c1': u'-5', u'name': u'女装'},
                {u'c1': u'-6', u'name': u'女装'},
                {u'c1': u'-7', u'name': u'女装'},
                {u'c1': u'-8', u'name': u'女装'},
                {u'c1': u'-9', u'name': u'女装'},
                {u'c1': u'-10', u'name': u'女装'}
                ]
    return render(request, 'dwxk/index.html', {'items': items, 'category': category})


def test(requset):
    return HttpResponse("welcome to test")
