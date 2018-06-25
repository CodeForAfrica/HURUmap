# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-25 13:45
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hurumap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataindicator',
            name='country',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='None'),
            preserve_default=False,
        ),
    ]
