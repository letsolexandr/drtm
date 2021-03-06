# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drtm', '0009_auto_20160906_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='street',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drtm.Street'),
        ),
        migrations.AddField(
            model_name='street',
            name='old_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
