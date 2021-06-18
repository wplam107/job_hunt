from restapi.jobs.models import Job
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from restapi.jobs.serializers import JobSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def job_list(request):
    # GET list of jobs, POST a new job, DELETE all jobs
    if request.method == 'GET':
        jobs = Job.objects.all()
        
        job_title = request.GET.get('job_title', None)
        if job_title is not None:
            jobs = jobs.filter(company__icontains=job_title)
        
        job_serializer = JobSerializer(jobs, many=True)
        return JsonResponse(job_serializer.data, safe=False)

    elif request.method == 'POST':
        job_data = JSONParser().parse(request)
        job_serializer = JobSerializer(data=job_data)
        if job_serializer.is_valid():
            job_serializer.save()
            return JsonResponse(job_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(job_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def job_detail(request, pk):
    # find job by pk (id)
    try: 
        job = Job.objects.get(pk=pk) 
    except Job.DoesNotExist: 
        return JsonResponse({'message': 'The job does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE job
    
        
@api_view(['GET'])
def job_list_responded(request):
    # GET all published jobs