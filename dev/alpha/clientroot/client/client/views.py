from rest_framework import viewsets
from client.client.serializers import *


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class RNN_MenuItemViewSet(viewsets.ModelViewSet):
    queryset = RNN_MenuItem.objects.all()
    serializer_class = RNN_MenuItemSerializer