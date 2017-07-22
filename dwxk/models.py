from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CategoryItems(models.Model):
    id = models.AutoField(primary_key=True)
    ds = models.IntegerField()
    ad_id = models.CharField(max_length=32)
    ad_name = models.TextField(null=True)
    coupon_value = models.FloatField()
    price = models.FloatField()
    img_url = models.URLField()
    coupon_url = models.URLField()
    c1 = models.IntegerField()
    sales_num = models.IntegerField()


class BrandInfo(models.Model):
    id = models.AutoField(primary_key=True)
    ds = models.IntegerField()
    brand_id = models.CharField(max_length=32)
    brand_name = models.TextField(null=True)
    brand_logo = models.URLField()


class BrandItems(models.Model):
    id = models.AutoField(primary_key=True)
    ds = models.IntegerField()
    ad_id = models.CharField(max_length=32)
    ad_name = models.TextField(null=True)
    coupon_value = models.FloatField()
    price = models.FloatField()
    img_url = models.URLField()
    coupon_url = models.URLField()
    brand_id = models.IntegerField()
    sales_num = models.IntegerField()


class ItemsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    ds = models.IntegerField()
    ad_id = models.CharField(max_length=32)
    ad_name = models.TextField(null=True)
    coupon_value = models.FloatField()
    price = models.FloatField()
    img_url = models.URLField()
    coupon_url = models.URLField()
    c1 = models.IntegerField()
    sales_num = models.IntegerField()
    brand_id = models.IntegerField(default=0)
    banner_id = models.IntegerField(default=0)


class BannerInfo(models.Model):
    id = models.AutoField(primary_key=True)
    ds = models.IntegerField()
    banner_id = models.IntegerField()
    keyword = models.TextField(null=True)
    img_url = models.URLField()


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    imei = models.TextField(null=True)
    ds = models.IntegerField()
    value = models.IntegerField(default=0)
    is_get = models.IntegerField(default=1)
    is_give = models.IntegerField(default=0)
