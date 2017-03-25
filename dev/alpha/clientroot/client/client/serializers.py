from rest_framework import serializers
from client.client.models import * #Client

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='client-highlight', format='html')

    class Meta:
        model = Client
        fields = ('url', 'id', #'highlight', 'owner',
                  'name') # , 'code', 'linenos', 'language', 'style')

class RNN_MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    # item_name = serializers.ReadOnlyField(source='item.name')
    # menu_name = serializers.ReadOnlyField(source='menu.name')
    iqs = Item.objects.all()
    mqs = Menu.objects.all()
    item_id = serializers.PrimaryKeyRelatedField(many=False, queryset=iqs) #source='item_set',
    menu_id = serializers.PrimaryKeyRelatedField(many=False, queryset=mqs) #source='menu_set'

    class Meta:
        model = RNN_MenuItem
        fields = ('url', 'id', #'highlight', 'owner',
                 'item_id', 'menu_id', 'price', )

    def create(self, validated_data):
        item_id = validated_data['item_id'].id
        menu_id = validated_data['menu_id'].id

        item = Item.objects.get(pk=item_id)
        menu = Menu.objects.get(pk=menu_id)
        price = validated_data['price']

        rnn = RNN_MenuItem.objects.create(item=item, menu=menu, price=price)
        return rnn

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    # items = serializers.HyperlinkedIdentityField(
    #     many=True,
    #     read_only=True,
    #     view_name='item-detail'
    # )

    items = RNN_MenuItemSerializer(source='rnn_menuitem_set', many=True, read_only=True)
    class Meta:
        model = Menu
        fields = ('url', 'id', 'items', #'highlight', 'owner',
                  'name') # , 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        name = validated_data['name']
        items = validated_data['items']
        if len(items) != 0:
            print('More than 0 items')
        menu = Menu.objects.create(name=name, items=items)
        return menu


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='client-highlight', format='html')

    class Meta:
        model = Item
        fields = ('url', 'id', #'highlight', 'owner',
                  'name') # , 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        name = validated_data['name']
        item = Item.objects.create(name=name)
        return item


