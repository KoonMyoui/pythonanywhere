# Generated by Django 3.1.2 on 2020-10-25 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0004_auto_20201025_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
