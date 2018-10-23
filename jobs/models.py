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

    class Meta:
        ordering = ['-end_date']

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    github_link = models.URLField('Github Link', blank=True, null=True)
    demo_link = models.URLField('Demo Link', blank=True, null=True)

    def __str__(self):
        return self.name

class Resume(models.Model):
    upload = models.FileField(upload_to='uploads')

class Technology(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey('Project', on_delete='CASCADE', related_name='technologies')

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'