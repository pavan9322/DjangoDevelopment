# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('user', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('mobno', models.IntegerField(max_length=10)),
            ],
        ),
    ]
