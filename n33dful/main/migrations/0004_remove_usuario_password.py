# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 17:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170501_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
    ]
