# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wavesapp', '0026_remove_gallery_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='profile_photos'),
        ),
    ]
