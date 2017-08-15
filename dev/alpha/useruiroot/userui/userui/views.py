from rest_framework import viewsets
from userui.userui.serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import userui.userui.kafkaInstance as ki
from core.kafka.KEvent import KEvent
from userui.userui.apps import UseruiappConfig

@api_view(['POST'])
def call_creation_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            kevent = KEvent(UseruiappConfig().name, 'order', 'w', __name__, request.data)
            ki.kEventManager.kgenerator.publish(kevent)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def call_order_add_item(request):
    if request.method == 'POST':
        serializer = RNN_OrderItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            kevent = KEvent(UseruiappConfig().name, 'order', 'w', __name__, request.data)
            ki.kEventManager.kgenerator.publish(kevent)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
