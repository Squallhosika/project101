from rest_framework import serializers
from order.order.models import *

class RNN_OrderItemSerializer(serializers.HyperlinkedModelSerializer):
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

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    items = RNN_OrderItemSerializer(source='rnn_orderitem_set', many=True, read_only=False)

    class Meta:
        model = Order
        fields = ('url', 'id', 'client_id', 'user_id', 'status', 'items')

    def create(self, validated_data):
        client_id = validated_data['client_id']
        user_id = validated_data['user_id']
        items_list = self.initial_data['items']
        c = len(items_list)
        if c == 0:
            order = Order.objects.create(client_id=client_id, user_id=user_id)
        else:
            order = Order.objects.create(client_id=client_id, user_id=user_id, items=items_list)

        return order

class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('url', 'id', 'name')
