# Generated by Django 5.1.1 on 2024-09-27 15:30

import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_profile_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='joined_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name=django.contrib.auth.models.User),
            preserve_default=False,
        ),
    ]
