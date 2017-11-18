# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

def index(request):
    blog_list = [
        {
            "blog_id": 1,
            "title": u"均匀分布随机数的生成算法简介",
            "introduction": u"""
             随机数是随机模拟的基本构成元素，其质量的优劣将直接影响模拟研究的成败。人们本能的可以通过物理实验产生一些常见分布的随机数，
             如可以通过反复的投硬币来产生二项分布的随机数，可以通过反复投骰子来产生多项分布的随机数，
             通过对排队的观察记录来产生泊松分布的随机数，该方法产生的随机数质量好，但是数量有限，而且成本很高。随后人们尝试预先生成大量的真实随机数存储起来，进行随机
            """
        },
        {
            "blog_id": 2,
            "title": u"随机模拟--抽样",
            "introduction": u"""
                某一球员在一次比赛中三分线外出手投篮n次，命中x次，那么该球员的三分球命中率为多少呢？
                频率学派与贝叶斯学派有不同的解答
               """
        }
    ]
    return render(request, "blog/index.html", {"blog_list": blog_list})


def get_blog_detail(request, blog_id):
    return render(request, "blog/blog_html/%s.html" % (blog_id,))
