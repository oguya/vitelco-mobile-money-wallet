# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_wallet_management', '0006_auto_20170316_1316'),
        ('wallet_transactions', '0010_auto_20170320_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletTopup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=64)),
                ('amount', models.IntegerField()),
                ('currency', models.CharField(default=b'KES', max_length=10)),
                ('bank_reference', models.CharField(max_length=64)),
                ('deposit_timestamp', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_wallet_management.CustomerWallet')),
            ],
            options={
                'verbose_name': 'Wallet Top-up',
                'verbose_name_plural': 'Wallet Top-ups',
            },
        ),
    ]