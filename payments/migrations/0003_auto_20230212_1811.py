# Generated by Django 3.2.9 on 2023-02-12 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20230212_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.item'),
        ),
    ]
