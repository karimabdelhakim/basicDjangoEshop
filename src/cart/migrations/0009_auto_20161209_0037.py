# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-09 00:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_cartproduct_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cart.Cart'),
        ),
    ]
