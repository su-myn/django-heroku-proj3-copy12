# Generated by Django 5.1.1 on 2024-10-06 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestay_app', '0012_repairlist_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='complainlist',
            name='day',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
