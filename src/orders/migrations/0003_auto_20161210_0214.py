# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-10 02:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20161210_0056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-timestamp']},
        ),
    ]
