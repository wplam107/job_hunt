from rest_framework import serializers 
from jobs.models import Job
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Job
        fields = (
            'id',
            'company',
            'job_title',
            'job_level',
            'min_years',
            'date_posted',
            'date_applied',
            'cover_letter',
            'response',
            'response_date'
        )