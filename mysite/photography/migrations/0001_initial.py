# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-22 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('url', models.CharField(max_length=260)),
            ],
        ),
    ]
