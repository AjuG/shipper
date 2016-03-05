# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shippers', '0001_initial'),
        ('jobs', '0002_job_porters'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='shipper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shippers.Shipper'),
        ),
    ]
