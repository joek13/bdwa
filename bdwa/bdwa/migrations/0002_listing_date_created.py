# Generated by Django 3.1.1 on 2020-09-12 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bdwa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]