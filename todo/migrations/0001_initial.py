# Generated by Django 2.0 on 2018-07-27 16:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('task_description', models.CharField(max_length=1000)),
                ('publish_time_stamp', models.DateTimeField(default=datetime.datetime(2018, 7, 27, 16, 50, 53, 986684, tzinfo=utc))),
                ('scheduled_end_time', models.DateTimeField()),
            ],
        ),
    ]
