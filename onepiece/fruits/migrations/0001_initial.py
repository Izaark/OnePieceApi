# Generated by Django 2.0.1 on 2018-02-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevilFruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('meaning', models.CharField(max_length=50)),
                ('fruit_type', models.IntegerField(choices=[(1, 'Paramecia'), (2, 'Logia'), (3, 'Zoan')])),
                ('abilities', models.TextField()),
                ('debilities', models.TextField()),
                ('apparence', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'DevilFruit',
                'verbose_name_plural': 'DevilFruits',
            },
        ),
    ]
