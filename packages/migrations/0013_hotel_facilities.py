# Generated by Django 4.0.3 on 2023-01-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0012_packages_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='facilities',
            field=models.CharField(default='Swimming pool, Buffet, and many more', max_length=500),
            preserve_default=False,
        ),
    ]
