# Generated by Django 3.1.2 on 2020-10-25 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0006_auto_20201025_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=50)),
                ('User_email', models.CharField(max_length=100)),
                ('User_msg', models.CharField(max_length=255)),
            ],
        ),
    ]