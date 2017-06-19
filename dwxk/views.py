from django.shortcuts import render
from django.http import HttpResponse
import urllib
import json


# Create your views here.


def index(request):
    url = "https://www.daweixinke.com/sqe.php?s=/CCKItem/getAdItemList"
    response = urllib.urlopen(url)
    result = json.load(response)
    items = []
    if (result == None):
        items = ""
    else:
        items = result["data"]["data"]
    return render(request, 'dwxk/index.html', {'items': items})
