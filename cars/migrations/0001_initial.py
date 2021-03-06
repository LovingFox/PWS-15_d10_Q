# Generated by Django 3.1.1 on 2020-09-21 07:21

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('issue_year', models.IntegerField()),
                ('transmission', models.SmallIntegerField(choices=[(1, 'механика'), (2, 'автомат'), (3, 'робот')])),
                ('color', colorfield.fields.ColorField(blank=True, default='', max_length=18)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
