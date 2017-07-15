from rest_framework import serializers
from dqueue.dqueue.models import *

class QueueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Queue
        fields = '__all__'  # ('url', 'id')

class NodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Node
        fields = '__all__'  # ('url', 'id', 'id_previous', 'id_next')
