# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 16:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('is_open', models.TimeField(db_index=True)),
                ('is_closed', models.TimeField(db_index=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-is_open'],
            },
        ),
    ]
