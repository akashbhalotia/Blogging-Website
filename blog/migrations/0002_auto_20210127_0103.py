# Generated by Django 2.2.17 on 2021-01-26 19:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 26, 19, 33, 6, 703334, tzinfo=utc)),
        ),
    ]
