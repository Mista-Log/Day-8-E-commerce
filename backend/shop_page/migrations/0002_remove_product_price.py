# Generated by Django 5.1.3 on 2024-11-28 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
