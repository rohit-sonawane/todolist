# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ('-date_created',)},
        ),
    ]