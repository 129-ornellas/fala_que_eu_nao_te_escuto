# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2023-02-09 20:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_metricas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricas',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]