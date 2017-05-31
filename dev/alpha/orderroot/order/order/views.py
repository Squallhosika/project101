from rest_framework import viewsets
from rest_framework import status
from rest_framework.parsers import JSONParser
from order.order.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class RNN_OrderItemViewSet(viewsets.ModelViewSet):
    queryset = RNN_OrderItem.objects.all()
    serializer_class = RNN_OrderItemSerializer

class RNN_QueueOrderViewSet(viewsets.ModelViewSet):
    queryset = RNN_QueueOrder.objects.all()
    serializer_class = RNN_QueueOrderSerializer

# class OrderFlowViewSet(viewsets.ModelViewSet):
#     queryset = OrderFlow.objects.all()
#     serializer_class = OrderFlowSerializer


@api_view(['GET'])
def get_orders_by_client_status(request):
    try:
        client_id = request.data.get('client_id')
        status = request.data.get('status')
        orders = Order.objects.filter(client_id=client_id, status=status)

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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)














def order_id_to_last_flow(request):
    try:
        order = Order.objects.get(id=request.data['order_id'])
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        return OrderFlow.objects.filter(order=order).latest('created')
    except OrderFlow.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def order_id_to_item_list(request):
    try:
        order = Order.objects.get(id=request.data['order_id'])
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        return RNN_OrderItem.objects.filter(order=order)
    except RNN_OrderItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def create_next_flow(order_flow, flow_status, employee_id=None):
    if not employee_id:
        employee_id = order_flow.employee_id
    return OrderFlow.objects.create(order=order_flow.order,
                                    client_id=order_flow.client_id,
                                    employee_id=employee_id,
                                    status=flow_status,
                                    rank=order_flow.rank)


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


@api_view(['POST'])
def place_order(request):
    # TODO check if it is ok to use request.data directly or
    # we have to use JSONParser
    # data = JSONParser().parse(request)
    try:
        order = Order.objects.get(id=request.data['order_id'])
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        queue = Queue.objects.filter(client_id=order.client_id).get()
        queue.last_rank += 1
        order_flow = OrderFlow.objects.create(order=order, client_id=order.client_id,
                                              status='PendingValidationClient', rank=queue.last_rank)
        queue.save()
        serializer = OrderFlowSerializer(order_flow, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def order_on_status(request, status):
    order_flow = OrderFlow.objects.filter(client_id=request.data['client_id'], status=status)

    if request.method == 'GET':
        serializer = OrderFlowSerializer(order_flow, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def new_orders(request):
    return order_on_status(request, 'PendingValidationClient')


@api_view(['GET'])
def beingserve_orders(request):
    return order_on_status(request, 'beingServe')


@api_view(['GET'])
def inqueue_orders(request):
    return order_on_status(request, 'accepted_by_client')


@api_view(['GET'])
def items_by_order(request):
    items = order_id_to_item_list(request)
    if request.method == 'GET':
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


def update_status_order(request, flow_status):
    order_flow = order_id_to_last_flow(request)
    if request.method == 'PUT':
        order_flow.status = flow_status
        order_flow.save()
        serializer = OrderFlowSerializer(order_flow, context={'request': request})
        return Response(serializer.data)


@api_view(['PUT'])
def order_accepted_by_client(request):
    return update_status_order(request, 'accepted_by_client')


@api_view(['PUT'])
def order_rejected_by_client(request):
    return update_status_order(request, 'rejected_by_client')


@api_view(['PUT'])
def order_canceled_by_user(request):
    return update_status_order(request, 'canceled_by_user')


@api_view(['PUT'])
def order_completed(request):
    return update_status_order(request, 'completed')


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
    try:
        queue = OrderFlow.objects.get(id=request.data['id'])
    except OrderFlow.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def last_orderflow(request):
    if request.method == 'GET':
        return order_id_to_last_flow(request)


@api_view(['PUT'])
def next_to_serve(request):
    client_id = request.data['client_id']
    employee_id = request.data['employee_id']
    try:
        queue = Queue.objects.get(client_id=client_id)
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        pos = queue.position
        while pos <= queue.last_rank:
            pos += 1
            try:
                order_flow = OrderFlow.objects.get(client_id=client_id, rank=pos)
                if order_flow.status != 'accepted_by_client':
                    continue
            except OrderFlow.DoesNotExist:
                continue
            order_flow.employee_id = employee_id
            order_flow.status = 'beingServe'
            order_flow.save()
            serializer = OrderFlowSerializer(order_flow, context={'request': request})
            return Response(serializer.data)
