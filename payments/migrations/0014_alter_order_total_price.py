# Generated by Django 3.2.9 on 2023-02-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0013_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
