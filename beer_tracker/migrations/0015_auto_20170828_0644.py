# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer_tracker', '0014_ratemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratemodel',
            old_name='user',
            new_name='beer',
        ),
    ]
