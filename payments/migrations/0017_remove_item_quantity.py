# Generated by Django 3.2.9 on 2023-02-15 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0016_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
    ]
