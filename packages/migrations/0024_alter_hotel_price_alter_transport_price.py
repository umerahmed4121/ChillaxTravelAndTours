# Generated by Django 4.1.5 on 2023-01-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0023_hotel_country_transport_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transport',
            name='price',
            field=models.IntegerField(),
        ),
    ]
