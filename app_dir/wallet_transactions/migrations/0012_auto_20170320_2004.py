# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_transactions', '0011_wallettopup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WalletTopup',
            new_name='WalletTopupTransaction',
        ),
        migrations.AlterModelOptions(
            name='wallettopuptransaction',
            options={'verbose_name': 'Wallet Top-up Transaction', 'verbose_name_plural': 'Wallet Top-up Transactions'},
        ),
    ]
