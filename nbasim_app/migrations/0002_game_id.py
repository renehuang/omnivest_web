# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-06 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbasim_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
