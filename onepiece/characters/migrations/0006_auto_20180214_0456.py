# Generated by Django 2.0.1 on 2018-02-14 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_affilation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Affilation',
            new_name='Affilations',
        ),
    ]