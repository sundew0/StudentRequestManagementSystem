# Generated by Django 5.0.6 on 2024-06-20 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentSupport', '0002_remove_studenthelp_classcode_remove_studenthelp_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenthelp',
            name='reason',
            field=models.CharField(choices=[('HAND_UP', 'hand_up'), ('toilet', 'toilet'), ('WATER', 'water')], default='water', max_length=9),
            preserve_default=False,
        ),
    ]
