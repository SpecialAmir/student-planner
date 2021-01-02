from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Plan(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField(default = timezone.now)
    summery = models.TextField(max_length = 4444)
    sum_of_studied_time = models.IntegerField()
    def __str__(self):
        return str(self.date)
