# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_comment_film'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='film',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.Film'),
            preserve_default=False,
        ),
    ]
