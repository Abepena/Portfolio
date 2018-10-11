from django.db import models
import datetime

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date',blank=True, null=True)

    def __str__(self):
        return self.name
