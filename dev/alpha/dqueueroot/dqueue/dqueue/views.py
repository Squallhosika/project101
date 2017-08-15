from rest_framework import viewsets
from dqueue.dqueue.serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


def node_move(node, nb_rank):
    remove_from_queue(node)
    insert(node, nb_rank)


def remove_from_queue(node):
    if node.id_next:
        node_next = Node.objects.get(pk=node.id_next)
        node_next.id_previous = node.id_previous
        node_next.save()
        if not node.id_previous:
            node.queue.node_id_first = node_next.id
            node.queue.save()

    if node.id_previous:
        node_previous = Node.objects.get(pk=node.id_previous)
        node_previous.id_next = node.id_next
        node_previous.save()
        if not node.id_next:
            node.queue.node_id_last = node_previous.id
            node.queue.save()

    node.id_previous = None
    node.id_next = None

    node.save()


def insert(node, nb_rank):
    node_id_first = node.queue.node_id_first
    current_node = Node.objects.get(pk=node_id_first)
    i = 1
    while current_node.id_next and i < nb_rank:
        current_node = Node.objects.get(pk=current_node.id_next)

    if i == nb_rank and current_node.id_next:
        node_place(node, current_node, True)
    else:
        node_place(node, current_node, False)


def node_place(node, node_displaced, place_before):
    if place_before:
        node.id_previous = node_displaced.id_previous
        node.id_next = node_displaced.id
        node_displaced.id_previous = node.id
        if node.id_previous:
            node_previous = Node.objects.get(pk=node.id_previous)
            node_previous.id_next = node.id
            node_previous.save()
        node.save()
        node_displaced.save()
    else:
        node.id_next = node_displaced.id_next
        node.id_previous = node_displaced.id
        node_displaced.id_next = node.id
        if node.id_next:
            node_next = Node.objects.get(pk=node.id_next)
            node_next.id_previous = node.id
            node_next.save()
        node.save()
        node_displaced.save()


@api_view(['GET'])
def nodes_by_type(request):
    try:
        master_id = request.data.get('master_id')
        type_queue = request.data.get('type')
        number = int(request.data.get('number'))
        queue = Queue.objects.filter(master_id=master_id, type=type_queue).get()
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    id_first = queue.node_id_first
    current_node = Node.objects.get(id=id_first)
    nodes = [current_node]
    iterator = 1

    while current_node.id_next and iterator < number:
        current_node = Node.objects.get(id=current_node.id_next)
        nodes.append(current_node)
        iterator += 1

    if request.method == 'GET':
        serializer = NodeSerializer(nodes, data=request.data, many=True, context={'request': request})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_queue(request):
    if request.method == 'POST':
        master_id = int(request.data.get('master_id'))
        type_queue = request.data.get('type')
        que = Queue.objects.create(master_id=master_id, type=type_queue)
        que.save()
        return Response(status=status.HTTP_201_CREATED)

        # TODO remove the return obove decoment that and understand why its not working
        # serializer = QueueSerializer(que, data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_queue(request):
    try:
        pk = request.data.get('id')
        queue = Queue.objects.get(pk=pk)
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_node(request):
    if request.method == 'POST':
        master_id = request.data.get('master_id')
        type_queue = request.data.get('type')
        node_id = request.data.get('id')
        time = request.data.get('time')
        rating = request.data.get('rating')

        queue = Queue.objects.filter(master_id=master_id, type=type_queue).get()
        # TODO serialize the node to validate the creation
        node = ctr.QueueControl.add_node(queue, node_id, time, rating)
        return Response(status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def create_node_end(request):
#     if request.method == 'POST':
#
#         id_order = request.date.get('id_order')
#         try:
#             queue = Queue.objects.filter(master_id=master_id, type=type_queue)
#         except Queue.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         last = Node.objects.get(id=queue.node_id_last)


@api_view(['UPDATE'])
def reposition_node(request):
    try:
        id_node = request.data.get('id')
        node = Node.objects.get(pk=id_node)
    except Node.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'UPDATE':
        nb_rank = request.data.get('nbrank')
        node_move(node, nb_rank)
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def remove_node(request):
    try:
        id_node = request.data.get('id')
        node = Node.objects.get(pk=id_node)
    except Node.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    remove_from_queue(node)
    node.delete()
    # node.save()
    return  Response(status=status.HTTP_204_NO_CONTENT)
