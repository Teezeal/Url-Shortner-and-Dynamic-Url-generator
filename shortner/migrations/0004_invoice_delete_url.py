# Generated by Django 4.2 on 2023-05-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_alter_url_original_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('invoice_number', models.CharField(max_length=50)),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('dynamic_url', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Url',
        ),
    ]
