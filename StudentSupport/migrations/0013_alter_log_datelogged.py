# Generated by Django 5.0.6 on 2024-06-21 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentSupport', '0012_alter_log_datelogged'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='datelogged',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 12, 36, 9, 869012, tzinfo=datetime.timezone.utc), verbose_name='Date Logged'),
        ),
    ]
