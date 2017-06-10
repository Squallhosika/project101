from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

from geo.geo.serializers import *



# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_client(request):
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def client_around(request):
    try:
        # point = Point(51.521219, -0.0777986) #POINT (51.521219 -0.0777986)
        # user=User.objects.filter(pk=2)
        # for u in user:
        #     point = u.last_location
        #     radius = u.preferred_radius/10

        latitude = float(request.data.get('latitude'))
        longitude = float(request.data.get('longitude'))

        point = Point(latitude, longitude)
        radius = request.data.get('radius')

        # point = Point(x=longitude,y=latitude)
        close_clients = Client.objects.filter(location__distance_lte=(point, D(km=radius)))

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(close_clients, context={'request': request}, many=True)
        return Response(serializer.data)