from rest_framework import viewsets
from rest_framework import status
from order.order.serializers import *
import order.order.controller as ctr
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.app.api.base import call_function


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class RNN_OrderItemViewSet(viewsets.ModelViewSet):
    queryset = RNN_OrderItem.objects.all()
    serializer_class = RNN_OrderItemSerializer


@api_view(['GET'])
def get_orders_by_client_status(request):
    try:
        client_id = request.data.get('client_id')
        status_order = request.data.get('status')
        orders = Order.objects.filter(client_id=client_id, status=status_order)

    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(orders, context={'request': request}, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def order_validate(request):
    try:
        pk = request.data.get('id')
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid() and request.data['status'] == 'validated':
            # TODO for now an order is automatically add to the Queue
            # Do we want that ? At this place it is sure that we do not want
            order_to_queue(order)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def order_pickup(request):
    try:
        pk = request.data.get('id')
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid() and request.data['status'] == 'pickup':
            call_function('DELETE', 'dqueue', 'deletenode', {'id': order.id})
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def order_id_to_item_list(request):
    try:
        order = Order.objects.get(id=request.data['order_id'])
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        return RNN_OrderItem.objects.filter(order=order)
    except RNN_OrderItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def order_to_queue(order):
    time = ctr.OrderControl.estimated_time(order)
    # TODO implement that and then remove fixe rating
    # rating_req = call_function('GET', 'user', 'userrating')
    # rating = rating_req['rating']
    rating = 4.5
    queue_id = ctr.OrderControl.queue_id(order)
    params = {'id': order.id, 'queue_id': queue_id, 'time': time, 'rating': rating}
    call_function('POST', 'dqueue', 'createnode', params)


@api_view(['POST'])
def create_item(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_item(request):
    try:
        id = request.data.get('id')
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def order_add_item(request):
    if request.method == 'POST':
        serializer = RNN_OrderItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def items_by_order(request):
    items = order_id_to_item_list(request)
    if request.method == 'GET':
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

