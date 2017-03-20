# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_transactions', '0010_auto_20170320_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='trid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
