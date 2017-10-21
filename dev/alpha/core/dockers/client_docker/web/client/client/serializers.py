from rest_framework import serializers
from client.client.models import * #Client

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

class RNN_ClientMenuSerializer(serializers.HyperlinkedModelSerializer):
    # item_name = serializers.ReadOnlyField(source='item.name')
    # menu_name = serializers.ReadOnlyField(source='menu.name')
    mqs = Menu.objects.all()
    cqs = Client.objects.all()
    menu_id = serializers.PrimaryKeyRelatedField(many=False, queryset=mqs) #source='menu_set'
    client_id = serializers.PrimaryKeyRelatedField(many=False, queryset=cqs) #source='item_set',

    class Meta:
        model = RNN_ClientMenu
        fields = ('url', 'id', #'highlight', 'owner',
                 'menu_id', 'client_id', 'status', )

    def create(self, validated_data):

        menu_id = validated_data['menu_id'].id
        client_id = validated_data['client_id'].id

        menu = Menu.objects.get(pk=menu_id)
        client = Client.objects.get(pk=client_id)
        status = validated_data['status']

        rnn = RNN_ClientMenu.objects.create(menu=menu, client=client, status=status)
        return rnn




class ClientSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    # items = serializers.HyperlinkedIdentityField(
    #     many=True,
    #     read_only=True,
    #     view_name='item-detail'
    # )
    menus = RNN_ClientMenuSerializer(source='rnn_clientmenu_set', many=True, read_only=False)
    class Meta:
        model = Client
        fields = ('url', 'id',  #'highlight', 'owner',
                  'menus', 'name', ) # , 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        name = validated_data['name']
        # itemL = self.data['items']
        menus_list = self.initial_data['menus']
        c = len(menus_list)
        if c==0:
            client = Client.objects.create(name=name)

        else:
            # for item in items_list:
            client = Client.objects.create(name=name, items=menus_list) #, item=item.id)


        return client

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    # items = serializers.HyperlinkedIdentityField(
    #     many=True,
    #     read_only=True,
    #     view_name='item-detail'
    # )
    items = RNN_MenuItemSerializer(source='rnn_menuitem_set', many=True, read_only=False)
    class Meta:
        model = Menu
        fields = ('url', 'id',  #'highlight', 'owner',
                  'items', 'name', ) # , 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        name = validated_data['name']
        # itemL = self.data['items']
        items_list = self.initial_data['items']
        c = len(items_list)
        if c==0:
            menu = Menu.objects.create(name=name)

        else:
            # for item in items_list:
            menu = Menu.objects.create(name=name, items=items_list) #, item=item.id)


        return menu

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='client-highlight', format='html')

    class Meta:
        model = Item
        fields = ('url', 'id', #'highlight', 'owner',
                  'name') # , 'code', 'linenos', 'language', 'style')
