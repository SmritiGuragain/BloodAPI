# Generated by Django 4.2 on 2023-04-13 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doner',
            name='Category',
            field=models.CharField(choices=[('A+ve', 'A+ve'), ('A-ve', 'A-ve'), ('B+ve', 'B+ve'), ('B-ve', 'B-ve'), ('O+ve', 'O+ve'), ('O-ve', 'O-ve'), ('AB+ve', 'AB+ve'), ('AB-ve', 'AB-ve')], max_length=20),
        ),
    ]
