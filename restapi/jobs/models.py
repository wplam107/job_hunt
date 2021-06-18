from django.db import models


class Job(models.Model):
    company = models.CharField(max_length=64, blank=False, default='')
    job_title = models.CharField(max_length=64, blank=False, default='')
    job_level = models.CharField(max_length=64, blank=True)
    min_years = models.IntegerField(null=True, blank=True)
    date_posted = models.DateField()
    date_applied = models.DateField()
    cover_letter = models.TextField(max_length=2500, blank=True)
    has_responded = models.BooleanField(default=False)
    response = models.CharField(max_length=16, blank=True)
    response_date = models.DateField(null=True, blank=True)
