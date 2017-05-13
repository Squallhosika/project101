from rest_framework import viewsets
from rest_framework import status
from rest_framework.parsers import JSONParser
from client.client.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class RNN_ClientMenuViewSet(viewsets.ModelViewSet):
    queryset = RNN_ClientMenu.objects.all()
    serializer_class = RNN_ClientMenuSerializer

class RNN_MenuItemViewSet(viewsets.ModelViewSet):
    queryset = RNN_MenuItem.objects.all()
    serializer_class = RNN_MenuItemSerializer

@api_view(['GET'])
def get_client_around_me(request):
    data = JSONParser().parse(request)
    try:
        close_clients = Client.objects.get(position=data['position'])
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(close_clients)
        return Response(serializer.data)

@api_view(['POST'])
def create_profile(request): # name, location, details, opening_hours): pass
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_profile(request):
    pass
    # try:
    #     client = Client.Ob
    # except Client.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_profile(request):
    data = JSONParser().parse(request)
    try:
        client = Client.objects.get(id=data['id'])
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_status(request):
    data = JSONParser().parse(request)
    try:
        client = Client.objects.get(id=data['id'])
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        client.active = data['active']
        client.save()
        serializer = ClientSerializer(client)
        return Response(serializer.data)

@api_view(['POST'])
def create_menu(request):
    if request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_menu():
    pass

@api_view(['GET'])
def search_item(request):
    data = JSONParser().parse(request)
    try:
        item = Item.objects.get(id=data['name'])
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

@api_view()
def create_item(): pass
def update_item(): pass
def create_barman(): pass
def update_barman(): pass
def update_barman_status(): pass
def create_shift(): pass
def addTo_shift(): pass
def remove_to_shift(): pass
def update_work_flow(): pass