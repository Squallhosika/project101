from rest_framework import serializers
from order.order.models import *

class RNN_OrderItemSerializer(serializers.HyperlinkedModelSerializer):

    # TODO Check this part do we load all the objects:
    iqs = Item.objects.all()
    oqs = Order.objects.all()

    item_id = serializers.PrimaryKeyRelatedField(many=False, queryset=iqs)
    order_id = serializers.PrimaryKeyRelatedField(many=False, queryset=oqs)

    class Meta:
        model = RNN_OrderItem
        fields = ('url', 'id', 'item_id', 'order_id', 'price', 'quantity')

    def create(self, validated_data):
        item_id = validated_data['item_id'].id
        order_id = validated_data['order_id'].id

        item = Item.objects.get(pk=item_id)
        order = Order.objects.get(pk=order_id)

        price = validated_data['price']
        quantity = validated_data['quantity']

        rnn = RNN_OrderItem.objects.create(item=item, order=order, price=price, quantity=quantity)
        return rnn

class RNN_QueueOrderSerializer(serializers.HyperlinkedModelSerializer):
    oqs = Order.objects.all()
    qqs = Queue.objects.all()

    order_id = serializers.PrimaryKeyRelatedField(many=False, queryset=oqs) #source='menu_set'
    queue_id = serializers.PrimaryKeyRelatedField(many=False, queryset=qqs) #source='item_set',

    class Meta:
        model = RNN_QueueOrder
        fields = ('url', 'id', 'order_id', 'queue_id', 'order_rank', 'employee_id', )

    def create(self, validated_data):
        order_id = validated_data['order_id'].id
        queue_id = validated_data['queue_id'].id

        order = Order.objects.get(pk=order_id)
        queue = Queue.objects.get(pk=queue_id)

        rank = validated_data['rank']
        employee_id = validated_data['employee_id']

        rnn = RNN_QueueOrder.objects.create(order=order, queue=queue, rank=rank, employee_id=employee_id)
        return rnn


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('url', 'id', 'name', 'item_id')

class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = ('url', 'id', 'status', 'client_id', 'menu_id', 'user_id')

class QueueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Queue
        fields = ('url', 'id', 'client_id', 'current_rank', 'last_rank')


# class OrderFlowSerializer(serializers.HyperlinkedModelSerializer):
#
#     oqs = Order.objects.all()
#     order_id = serializers.PrimaryKeyRelatedField(many=False, queryset=oqs)
#
#     class Meta:
#         model = OrderFlow
#         fields = ('url', 'id', 'order_id', 'client_id', 'employee_id', 'status', 'rank')
