# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_auto_20180107_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treenode',
            name='key',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]