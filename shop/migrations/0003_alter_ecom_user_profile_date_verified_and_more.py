# Generated by Django 4.0 on 2021-12-29 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_ecom_user_profile_aadhar_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecom_user_profile',
            name='date_verified',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 8, 55, 4, 229077)),
        ),
        migrations.AlterField(
            model_name='ecom_user_profile',
            name='phone_number',
            field=models.CharField(max_length=16),
        ),
    ]
