# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 10:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wavesapp', '0006_booking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Appointment',
        ),
        migrations.DeleteModel(
            name='Bookings',
        ),
    ]
