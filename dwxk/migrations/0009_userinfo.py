# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-22 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwxk', '0008_auto_20170720_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imei', models.TextField(null=True)),
                ('ds', models.IntegerField()),
                ('value', models.TextField(default=0)),
            ],
        ),
    ]
