# Generated by Django 4.1.3 on 2022-11-12 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_dailyvitals_blood_pressure_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyvitals',
            name='heartrate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]