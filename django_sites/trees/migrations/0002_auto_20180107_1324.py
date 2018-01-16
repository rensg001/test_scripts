# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treenode',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='treenode',
            name='key',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='treenode',
            name='parent_key',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
