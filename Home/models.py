
# Create your models here.
from django.db import models


class Progress(models.Model):
    ip = models.CharField(max_length=20)
    status_type = models.IntegerField()
    percent = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)

# status_type = 0: client connected
# status_type = 1: processing
# status_type = 2: completed
