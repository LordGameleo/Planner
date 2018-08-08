from django.db import models
from datetime import datetime
import django.utils.timezone

class Task(models.Model):
    task_title = models.CharField(max_length = 100)
    task_description = models.CharField(max_length = 1000)
    publish_time_stamp = models.DateTimeField(default = django.utils.timezone.now)
    scheduled_end_time = models.DateTimeField(default = django.utils.timezone.now)
    task_done_flag = models.BooleanField(default = False)
    def __str__(self):
        display_tag = "'" + str(self.task_title) + "' - " + " to be completed by - " +str(self.publish_time_stamp.date())
        return display_tag
