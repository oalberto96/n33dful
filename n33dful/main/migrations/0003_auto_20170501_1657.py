# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 16:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170501_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nickname',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]