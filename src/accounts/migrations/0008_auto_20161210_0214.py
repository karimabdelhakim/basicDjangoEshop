# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-10 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20161210_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='creditCard',
            field=models.CharField(max_length=15),
        ),
    ]
