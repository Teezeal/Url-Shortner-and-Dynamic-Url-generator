# Generated by Django 4.2 on 2023-05-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.CharField(max_length=2000),
        ),
    ]
