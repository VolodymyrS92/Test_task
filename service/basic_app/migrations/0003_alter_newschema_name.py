# Generated by Django 3.2.7 on 2022-01-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20220103_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newschema',
            name='name',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
