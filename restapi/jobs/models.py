from django.db import models
from django.utils.translation import gettext_lazy as _


class Job(models.Model):
    class JobLevel(models.TextChoices):
        NO_LEVEL = "N", _("No Level")
        INTERN = "I", _("Intern")
        ENTRY = "E", _("Entry Level")
        ASSOCIATE = "A", _("Associate")
        MID_SENIOR = "M", _("Mid-Senior")
        DIRECTOR = "D", _("Director")

    class Response(models.TextChoices):
        NO_RESPONSE = "N", _("No Response")
        REJECTION = "R", _("Rejection")
        FOLLOW_UP = "F", _("Follow Up")
        INTERVIEW = "I", _("Interview")

    class CoverLetter(models.TextChoices):
        YES = "Yes", _("Yes")
        NO = "No", _("No")

    company = models.CharField(max_length=64, blank=False, default='')
    job_title = models.CharField(max_length=64, blank=False, default='')
    job_level = models.CharField(max_length=16, choices=JobLevel.choices, default=JobLevel.NO_LEVEL)
    min_years = models.IntegerField(null=True, blank=True)
    date_posted = models.DateField()
    date_applied = models.DateField()
    cover_letter = models.CharField(max_length=16, choices=CoverLetter.choices, default=CoverLetter.NO)
    response = models.CharField(max_length=16, choices=Response.choices, default=Response.NO_RESPONSE)
    response_date = models.DateField(null=True, blank=True)
