# Generated by Django 5.0.6 on 2024-06-21 04:18

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentSupport', '0018_rename_user_id_log_user_alter_log_datelogged'),
        ('accounts', '0012_alter_classlist_classid_alter_classlist_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='datelogged',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 14, 18, 31, 609406, tzinfo=datetime.timezone.utc), verbose_name='Date Logged'),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
    ]
