import requests
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect, HttpResponse


mapper = {
    'geo': 'localhost:8001',
    'order': 'localhost:8003',
    'client': 'localhost:8004',
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

