from django.shortcuts import render
from django.http import HttpResponse
import urllib
import urllib2
import json


# Create your views here.


def index(request):
    url = "https://www.daweixinke.com/sqe.php"
    items = []
    for page in range(1, 11):
        parameter = "?s=/CCKItem/getAdItemList&pageNum=10&order_status=10&page="
        response = urllib.urlopen(url + parameter + str(page))
        result = json.load(response)
        if (result != None):
            items = items + result["data"]["data"]

    for item in items:
        adId = "&data[adId]=%s" % (item["ad_id"])
        itemId = "&data[itemId]=%s" % (item["item_id"])
        adZoneId = "&data[adZoneId]=18557"
        addSource = "&data[add_source]=home"
        isVideo = "&data[isVideo]=0"
        platform = "&data[platform]=web"
        data = adId + itemId + adZoneId + addSource + isVideo + platform
        coupon = getCoupon(data)
        item["coupon"] = coupon

    return render(request, 'dwxk/index.html', {'items': items})


def getCoupon(data):
    url = "https://www.daweixinke.com/sqe.php?s=/CCKItem/addCCKItem"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'charset': 'UTF-8',
        'Cookie': 'UM_distinctid=15b2a27ba8581-01c694495-66121479-15f900-15b2a27ba88cc; cck_access_token=E39E77BAF9D80C3CFEE2529120D8048C; C NZZDATA1261673522=1222127928-1497702020-https%253A%252F%252Fwww.daweixinke.com%252F%7C1497702020; PHPSESSID=9goqo4bnidkigl5qt2c40kips4; CNZ ZDATA1261294143=8452916-1491059078-https%253A%252F%252Fwww.baidu.com%252F%7C1497887195'
    }
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    result = json.load(response)
    coupon = result["data"]["couponShare"]["discount_url"]
    return coupon
