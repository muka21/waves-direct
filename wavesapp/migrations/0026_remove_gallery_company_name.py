# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wavesapp', '0025_auto_20171017_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='company_name',
        ),
    ]
