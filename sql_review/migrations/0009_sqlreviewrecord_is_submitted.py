# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_review', '0008_sqlbackuprecord_backup_db_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqlreviewrecord',
            name='is_submitted',
            field=models.BooleanField(default=0, verbose_name='\u662f\u5426\u63d0\u4ea4\u81f3\u5ba1\u6838'),
        ),
    ]