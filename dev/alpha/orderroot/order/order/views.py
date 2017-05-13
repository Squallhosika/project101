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


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


def order_id_to_position(request):
    data = JSONParser().parse(request)
    try:
        order = Order.objects.get(id=data['order_id'])
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        return Position.objects.get(order=order)
    except Position.DoesNotExist:
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
def order_items(request):
    items = order_id_to_item_list(request)
    if request.method == 'GET':
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def update_order():
    pass


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
        positions = Position.objects.filter(queue=queue)
        # TODO maybe there is a better way to do that
        ranks = [pos.position for pos in positions]
        new_rank = max(ranks) + 1
        position = Position.objects.create(order=order, queue=queue, position=new_rank)
        serializer = PositionSerializer(instance=position, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def cancel_order():
    pass


@api_view(['PUT'])
def complete_order():
    pass


@api_view(['GET'])
def queue_position(request):
    position = order_id_to_position(request)
    if request.method == 'GET':
        serializer = PositionSerializer(position)
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

@api_view(['PUT'])
def update_queue():
    pass


def manage_work_flow(): pass
def update_work_flow(): pass
def get_queue(): pass
def get_next_to_serve(): pass
def get_queue_update(): pass