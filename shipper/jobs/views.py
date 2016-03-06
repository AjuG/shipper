import json

from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from jobs.models import Job
from jobs.serializers import JobSerializer

from porters.models import Porter

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
            if job.status in [6]:
                job_status = 'Fulfilled'
            else:
                job_status = 'Pending'
            data_dict = {"uid":job.uid, 
                    'status': job_status, 
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
                    'status': 'Pending', 
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
                    'status': 'Pending', 
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
def complete_job_list(request):
    """
    List all jobs, or create a job.
    """
    if request.method == 'GET':
        queryset = Job.objects.filter(status__in=[6]).order_by('-created_at')
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
                    'status': 'Fulfilled', 
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
def job_detail(request, uid):
    """
    Retrieve, update or delete a job.
    """
    try:
        job = Job.objects.get(uid=uid)
    except Job.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
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
        print data_dict
        return JSONResponse(data_dict)

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


@csrf_exempt
def get_available_porter(request, job_uid, search_radius):
    try:
        job = Job.objects.get(pk=job_uid)
    except Job.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        if job.status in [0,1,2,3]: #in job status
            destination = job.pickup_location
        else:
            destination = job.drop_location
        nearby_porters = Porter.objects.filter(
            current_location__dwithin=(destination, 0.01*int(search_radius))
        )
        data = list()
        for porter in nearby_porters:
            distance = destination.distance(porter.current_location)
            data_dict = {
                'name': porter.name,
                'phone': porter.phone,
                'rating': porter.rating,
                'average_quote': porter.average_quote,
                'distance': distance,
            }
            data.append(data_dict)
        return JSONResponse(data_dict)
