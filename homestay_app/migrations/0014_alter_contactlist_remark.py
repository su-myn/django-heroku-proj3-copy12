# Generated by Django 5.1.1 on 2024-10-06 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestay_app', '0013_complainlist_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactlist',
            name='remark',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
