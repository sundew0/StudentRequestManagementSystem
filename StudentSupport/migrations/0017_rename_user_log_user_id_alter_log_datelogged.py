# Generated by Django 5.0.6 on 2024-06-21 02:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentSupport', '0016_alter_log_datelogged_remove_log_user_log_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='log',
            name='datelogged',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 12, 45, 43, 371248, tzinfo=datetime.timezone.utc), verbose_name='Date Logged'),
        ),
    ]
