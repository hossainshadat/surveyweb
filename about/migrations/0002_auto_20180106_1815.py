# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-06 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audit_report',
            options={'verbose_name': 'Audit report', 'verbose_name_plural': 'Audit report'},
        ),
        migrations.AlterModelOptions(
            name='human_resource',
            options={'verbose_name': 'Organization abstract', 'verbose_name_plural': 'Organization abstract'},
        ),
        migrations.AlterModelOptions(
            name='organization_abstract',
            options={'verbose_name': 'Organization abstract', 'verbose_name_plural': 'Organization abstract'},
        ),
    ]
