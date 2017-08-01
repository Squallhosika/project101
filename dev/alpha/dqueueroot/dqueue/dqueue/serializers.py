from rest_framework import serializers
from dqueue.dqueue.models import *
import dqueue.dqueue.controller as ctr


class QueueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Queue
        fields = ('url', 'id', 'master_id', 'type', 'node_id_first', 'node_id_last')


class NodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Node
        fields = ('url', 'id', 'id_previous', 'id_next', 'queue', 'time', 'rating')

    # def create(self, validated_data):
    #     master_id = validated_data.get('master_id')
    #     type_queue = validated_data.get('type')
    #     node_id = validated_data['id']
    #     time = validated_data['time']
    #     rating = validated_data['rating']
    #
    #     queue = Queue.objects.filter(master_id=master_id, type=type_queue)
    #     node = ctr.QueueControl.add_node(queue, node_id, time, rating)
    #
    #     return node
