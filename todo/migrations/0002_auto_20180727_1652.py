# Generated by Django 2.0 on 2018-07-27 16:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='publish_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 27, 16, 52, 1, 91201, tzinfo=utc)),
        ),
    ]
