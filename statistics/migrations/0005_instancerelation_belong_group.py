# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('statistics', '0004_remove_instancerelation_belong_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='instancerelation',
            name='belong_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    to='statistics.MysqlInstanceGroup', verbose_name='Mysql \u7ec4'),
        ),
    ]