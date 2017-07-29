from rest_framework import serializers
from dqueue.dqueue.models import *
import dqueue.dqueue.controller as ctr


class QueueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Queue
        fields = '__all__'  # ('url', 'id')


class NodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Node
        fields = '__all__'  # ('url', 'id', 'id_previous', 'id_next')

    def create(self, validated_data):
        node_id = validated_data['id']
        queue_id = validated_data['queue_id']
        time = validated_data['time']
        rating = validated_data['rating']

        queue = Queue.objects.get(pk=queue_id)
        node = ctr.QueueControl.add_node(queue, node_id, time, rating)

        return node
