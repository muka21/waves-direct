# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wavesapp', '0029_auto_20171018_0949'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='wine',
        ),
        migrations.AddField(
            model_name='review',
            name='Profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='wavesapp.Profile'),
        ),
        migrations.DeleteModel(
            name='Wine',
        ),
    ]