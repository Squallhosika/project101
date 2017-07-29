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


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'  # ('url', 'id', 'name', 'item_id')


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'  # ('url', 'id', 'status', 'shift_id', 'client_id', 'menu_id', 'user_id')
