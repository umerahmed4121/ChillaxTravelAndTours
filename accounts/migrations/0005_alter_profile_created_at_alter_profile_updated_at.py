# Generated by Django 4.1.5 on 2023-01-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
