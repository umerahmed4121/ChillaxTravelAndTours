# Generated by Django 4.1.5 on 2023-01-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0021_packages_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='price',
            field=models.IntegerField(),
        ),
    ]
