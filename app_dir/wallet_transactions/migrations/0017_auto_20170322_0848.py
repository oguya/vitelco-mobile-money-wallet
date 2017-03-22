# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_wallet_management', '0008_auto_20170320_1550'),
        ('wallet_transactions', '0016_merge_20170321_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='DebitMandate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(default=b'KES', max_length=10)),
                ('amount_limit', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('number_of_payments', models.IntegerField()),
                ('frequecy_type', models.CharField(choices=[(b'weekly', b'weekly'), (b'fortnight', b'fortnight'), (b'monthspecificdate', b'monthspecificdate'), (b'twomonths', b'twomonths'), (b'threemonths', b'threemonths'), (b'fourmonths', b'fourmonths'), (b'sixmonths', b'sixmonths'), (b'yearly', b'yearly'), (b'lastdaymonth', b'lastdaymonth'), (b'lastdaymonthworking', b'lastdaymonthworking'), (b'lastmonday', b'lastmonday'), (b'lasttuesday', b'lasttuesday'), (b'lastwednesday', b'lastwednesday'), (b'lastthursday', b'lastthursday'), (b'lastfriday', b'lastfriday'), (b'lastsaturday', b'lastsaturday'), (b'lastsunday', b'lastsunday'), (b'specificdaymonthly', b'specificdaymonthly')], max_length=20)),
                ('mandate_status', models.CharField(choices=[(b'active', b'active'), (b'inactive', b'inactive')], max_length=20)),
                ('requestDate', models.DateTimeField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_wallet_management.CustomerWallet')),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='request_date',
        ),
    ]