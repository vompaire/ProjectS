# Generated by Django 4.1.5 on 2023-02-14 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='price',
        ),
        migrations.RemoveField(
            model_name='new',
            name='quantity',
        ),
    ]
