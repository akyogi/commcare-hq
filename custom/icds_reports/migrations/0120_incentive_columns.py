# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-15 21:31
from __future__ import unicode_literals, absolute_import

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0119_distribute_tables')
    ]

    operations = [
        migrations.AddField(
            model_name='awwincentivereport',
            name='awh_eligible',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='awwincentivereport',
            name='incentive_eligible',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='awwincentivereport',
            name='is_launched',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='awwincentivereport',
            name='visit_denominator',
            field=models.SmallIntegerField(null=True),
        ),
    ]
