# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-07 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='location',
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='publication_link',
            name='location',
            field=models.ImageField(blank=True, default=1, null=True, upload_to='survey-detail'),
        ),
        migrations.AddField(
            model_name='publication_link',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]