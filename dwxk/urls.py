"""coupon URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^index/$', views.index),
    url(r'^search/$', views.get_search, name='get_search'),
    url(r'^category/(?P<cid>-[0-9]+)/(?P<cname>.+)/$', views.get_category, name='get_category'),

    url(r'^api/get_brand_info/(?P<page>[0-9]+)/$', views.get_brand_info),
    url(r'^api/get_category_info/$', views.get_category_info),
    url(r'^api/get_category_items/(?P<cid>-[0-9]+)/(?P<page>[0-9]+)/$', views.get_category_items),
]
