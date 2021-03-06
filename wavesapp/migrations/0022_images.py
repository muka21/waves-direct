# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wavesapp', '0021_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_photos', verbose_name='Image')),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wavesapp.Profile')),
            ],
        ),
    ]
