# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 04:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_remove_customer_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_customer', to='customer.Customer'),
        ),
    ]