from rest_framework import serializers
from order.order.models import *


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('url', 'id', 'name')


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = ('url', 'id', 'client_id', 'user_id')


class OrderFlowSerializer(serializers.HyperlinkedModelSerializer):

    oqs = Order.objects.all()
    order_id = serializers.PrimaryKeyRelatedField(many=False, queryset=oqs)

    class Meta:
        model = OrderFlow
        fields = ('url', 'id', 'order_id', 'client_id', 'employee_id', 'status', 'rank')


class QueueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Queue
        fields = ('url', 'id', 'client_id', 'position', 'last_rank')


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
