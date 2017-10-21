import requests
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect, HttpResponse


mapper = {
    'geo': 'localhost:7001',
    'order': 'localhost:7003',
    'client': 'localhost:7004',
}


def get_route(path):
    service = path.split('/')[1]
    return 'http://' + mapper.get(service) + path


def route(request):
    path = request.path
    url = get_route(path)

    return HttpResponse(requests.get(url, data=request.data))


@api_view(['GET'])
def get(request):
    return route(request)


@api_view(['POST'])
def post(request):
    return route(request)

