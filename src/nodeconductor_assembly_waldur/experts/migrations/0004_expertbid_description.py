# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-14 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0003_expertbid'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertbid',
            name='description',
            field=models.CharField(blank=True, max_length=500, verbose_name='description'),
        ),
    ]