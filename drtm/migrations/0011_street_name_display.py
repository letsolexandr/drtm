# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drtm', '0010_auto_20160906_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='street',
            name='name_display',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
