# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drtm', '0003_balans_service_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
