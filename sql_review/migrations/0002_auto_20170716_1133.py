# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqlreviewrecord',
            name='is_checked',
            field=models.BooleanField(default=0, verbose_name='\u662f\u5426\u901a\u8fc7\u4ee3\u7801\u5ba1\u6838'),
        ),
        migrations.AlterField(
            model_name='sqlreviewrecord',
            name='is_executed',
            field=models.BooleanField(default=0, verbose_name='\u662f\u5426\u6267\u884c\u5b8c\u6210'),
        ),
        migrations.AlterField(
            model_name='sqlreviewrecord',
            name='is_reviewed',
            field=models.BooleanField(default=0, verbose_name='\u662f\u5426\u9879\u76ee\u7ecf\u7406\u5ba1\u6838'),
        ),
    ]