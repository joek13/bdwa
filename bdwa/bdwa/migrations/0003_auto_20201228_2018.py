# Generated by Django 3.1.4 on 2020-12-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdwa', '0002_listing_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
