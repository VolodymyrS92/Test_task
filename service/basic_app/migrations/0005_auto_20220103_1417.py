# Generated by Django 3.2.7 on 2022-01-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_auto_20220103_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newschema',
            name='column_separator',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='newschema',
            name='string_character',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
