# Generated by Django 4.0.3 on 2023-01-03 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_transport_transportcategory_transportimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='color',
            field=models.CharField(default='White', max_length=200),
            preserve_default=False,
        ),
    ]
