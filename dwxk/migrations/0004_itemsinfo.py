# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-20 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwxk', '0003_auto_20170704_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ds', models.IntegerField()),
                ('ad_id', models.CharField(max_length=32)),
                ('ad_name', models.TextField(null=True)),
                ('coupon_value', models.FloatField()),
                ('price', models.FloatField()),
                ('img_url', models.URLField()),
                ('coupon_url', models.URLField()),
                ('c1', models.IntegerField()),
                ('sales_num', models.IntegerField()),
                ('brand_id', models.IntegerField()),
                ('banner_id', models.IntegerField()),
            ],
        ),
    ]
