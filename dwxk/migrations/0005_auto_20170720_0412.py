# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-20 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwxk', '0004_itemsinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsinfo',
            name='banner_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemsinfo',
            name='brand_id',
            field=models.IntegerField(default=0),
        ),
    ]
