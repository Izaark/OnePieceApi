# Generated by Django 2.0.1 on 2018-02-10 04:00

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('apparence', models.TextField()),
                ('epithet', models.CharField(max_length=200, unique=True)),
                ('bounty', models.IntegerField(default=0)),
                ('activities', models.CharField(max_length=250)),
                ('abilities', django.contrib.postgres.fields.jsonb.JSONField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Character',
                'verbose_name_plural': 'Characters',
            },
        ),
    ]