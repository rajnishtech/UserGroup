# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190502_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
