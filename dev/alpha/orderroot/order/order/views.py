from rest_framework import viewsets
from rest_framework import status
from rest_framework.parsers import JSONParser
from order.order.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class RNN_OrderItemViewSet(viewsets.ModelViewSet):
    queryset = RNN_OrderItem.objects.all()
    serializer_class = RNN_OrderItemSerializer


class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer


class OrderInQueueViewSet(viewsets.ModelViewSet):
    queryset = OrderInQueue.objects.all()
    serializer_class = OrderInQueueSerializer


def order_id_to_position(request):
    data = JSONParser().parse(request)
    try:
        order = Order.objects.get(id=data['order_id'])
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        return OrderInQueue.objects.get(order=order), order
    except OrderInQueue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def order_id_to_item_list(request):
    data = JSONParser().parse(request)
    try:
        order = Order.objects.get(id=data['order_id'])
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        return RNN_OrderItem.objects.filter(order=order)
    except RNN_OrderItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


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


@api_view(['POST'])
def place_order(request):
    data = JSONParser().parse(request)
    try:
        order = Order.objects.get(id=data['order_id'])
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        queue = Queue.objects.get(id=data['queue_id'])
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        orders_in_queue = OrderInQueue.objects.filter(queue=queue)
        # TODO maybe there is a better way to do that
        positions = [order.position for order in orders_in_queue]
        new_pos = max(positions) + 1
        order_in_queue = OrderInQueue.objects.create(order=order, queue=queue, position=new_pos)
        serializer = OrderInQueueSerializer(order_in_queue, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def end_order(request, status):
    order_in_queue, order = order_id_to_position(request)
    if request.method == 'PUT':
        pos = order_in_queue.position
        orders_in_queue = OrderInQueue.objects.filter(queue=order_in_queue.queue)
        # TODO can do better that the lop && belong to the business logic
        for ordq in orders_in_queue:
            if ordq.position > pos:
                ordq.position = ordq.position - 1
                ordq.save()
        order_in_queue.delete()
        order.status = status
        order.save()
        serializer = OrderSerializer(order, context={'request': request})
        return Response(serializer.data)


@api_view(['PUT'])
def cancel_order(request):
    return end_order(request, 'canceled')


@api_view(['PUT'])
def complete_order(request):
    return end_order(request, 'completed')


@api_view(['GET'])
def queue_position(request):
    position, _ = order_id_to_position(request)
    if request.method == 'GET':
        serializer = OrderInQueueSerializer(position)
        return Response(serializer.data)

# TODO for now just the position is enough
@api_view(['GET'])
def get_estimated_time():
    pass

@api_view(['POST'])
def create_queue(request):
    if request.method == 'POST':
        serializer = QueueSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_queue(request):
    data = JSONParser().parse(request)
    try:
        queue = Queue.objects.get(id=data['id'])
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def orders_in_queue(request):
    data = JSONParser().parse(request)
    try:
        queue = Queue.objects.get(id=data['queue_id'])
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    orders = OrderInQueue.obects.filter(queue=queue)

    if request.method == 'GET':
        serializer = OrderInQueueSerializer(orders, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['PUT'])
def order_status(request):
    data = JSONParser().parse(request)
    order_id = data['order_id']
    status = data['status']

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        order.status = status
        order.save()
        serializer = OrderSerializer(order, context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def next_to_serve(request):
    data = JSONParser().parse(request)
    try:
        queue = Queue.objects.get(id=data['queue_id'])
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    order_in_queue = OrderInQueue.obects.filter(queue=queue, position=1)

    if request.method == 'GET':
        serializer = OrderSerializer(order_in_queue.order, context={'request': request})
        return Response(serializer.data)
