from rest_framework import viewsets
from client.client.serializers import *


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