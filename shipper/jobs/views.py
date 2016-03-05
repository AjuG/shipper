import json

from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from jobs.models import Job
from jobs.serializers import JobSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def job_list(request):
    """
    List all jobs, or create a job.
    """
    if request.method == 'GET':
        queryset = Job.objects.all().order_by('-created_at')
        data = list()
        for job in queryset:
            try:
                pickup_json = json.loads(job.pickup_location.json)
            except:
                pickup_json = 'null'
            try:
                drop_json = json.loads(job.drop_location.json)
            except:
                drop_json = 'null'
            data_dict = {"uid":job.uid, 
                    'status': job.status, 
                    'pickup_location': pickup_json, 
                    'drop_location': drop_json,
                    'shipper': job.shipper.id,
                    'porters': job.porters.values_list('pk', flat=True),
                    'time_to_reach': job.time_to_reach,
                    'amount_offered': job.amount_offered,
                    'created_at': job.created_at
                    }
            data.append(data_dict)
        #serializer = JobSerializer(queryset, many=True)
        return JSONResponse(data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def pending_job_list(request):
    """
    List all jobs, or create a job.
    """
    if request.method == 'GET':
        queryset = Job.objects.filter(status__in=[0,1]).order_by('-created_at')
        data = list()
        for job in queryset:
            try:
                pickup_json = json.loads(job.pickup_location.json)
            except:
                pickup_json = 'null'
            try:
                drop_json = json.loads(job.drop_location.json)
            except:
                drop_json = 'null'
            data_dict = {"uid":job.uid, 
                    'status': job.status, 
                    'pickup_location': pickup_json, 
                    'drop_location': drop_json,
                    'shipper': job.shipper.id,
                    'porters': job.porters.values_list('pk', flat=True),
                    'time_to_reach': job.time_to_reach,
                    'amount_offered': job.amount_offered,
                    'created_at': job.created_at
                    }
            data.append(data_dict)
        return JSONResponse(data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def active_job_list(request):
    """
    List all jobs, or create a job.
    """
    if request.method == 'GET':
        queryset = Job.objects.filter(status__in=[2, 3, 4, 5]).order_by('-created_at')
        serializer = serialize('geojson', queryset,
          fields=('uid', 'status', 'pickup_location', 'drop_location', 'shipper', 'porters', 'time_to_reach', 'amount_offered', 'created_at'))
        return JSONResponse(serializer)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def complete_job_list(request):
    """
    List all jobs, or create a job.
    """
    if request.method == 'GET':
        queryset = Job.objects.filter(status__in=[6]).order_by('-created_at')
        serializer = serialize('geojson', queryset,
          fields=('uid', 'status', 'pickup_location', 'drop_location', 'shipper', 'porters', 'time_to_reach', 'amount_offered', 'created_at'))
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def job_detail(request, pk):
    """
    Retrieve, update or delete a job.
    """
    try:
        snippet = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = serialize('geojson', snippet,
          fields=('uid', 'status', 'pickup_location', 'drop_location', 'shipper', 'porters', 'time_to_reach', 'amount_offered', 'created_at'))
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = JobSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
