from django.db import models
from datetime import datetime
class Tasks(models.Model):
    task_title = models.CharField(max_length = 100)
    task_description = models.CharField(max_length = 1000)
    publish_time_stamp = models.DateTimeField(default = datetime.now())
    scheduled_end_time = models.DateTimeField()

    def __str__(self):
        display_tag = str(self.task_title) + str(self.publish_time_stamp.date())
        return display_tag
