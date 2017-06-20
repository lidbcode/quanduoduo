from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ItemsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    ds = models.IntegerField()
    ad_id = models.CharField(max_length=32)
    item_id = models.CharField(max_length=128)
    ad_name = models.TextField(null=True)
    coupon_value = models.FloatField()
    price = models.FloatField()
    img_url = models.URLField()
    coupon_url = models.URLField()
    c1 = models.IntegerField()
