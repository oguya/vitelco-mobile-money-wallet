# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_transactions', '0016_merge_20170321_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='request_date',
        ),
    ]
