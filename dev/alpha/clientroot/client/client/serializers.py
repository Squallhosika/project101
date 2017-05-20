from rest_framework import serializers
from client.client.models import * #Client

class RNN_MenuItemSerializer(serializers.HyperlinkedModelSerializer):
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
    mqs = Menu.objects.all()
    cqs = Client.objects.all()

    menu_id = serializers.PrimaryKeyRelatedField(many=False, queryset=mqs) #source='menu_set'
    client_id = serializers.PrimaryKeyRelatedField(many=False, queryset=cqs) #source='item_set',

    class Meta:
        model = RNN_ClientMenu
        fields = ('url', 'id', #'highlight', 'owner',
                 'menu_id', 'client_id', 'status', )

    def create(self, validated_data):

        # if 'menus_id' not in self.initial_data:

        menu_id = validated_data['menu_id'].id
        client_id = validated_data['client_id'].id

        menu = Menu.objects.get(pk=menu_id)
        client = Client.objects.get(pk=client_id)
        status = validated_data['status']

        rnn = RNN_ClientMenu.objects.create(menu=menu, client=client, status=status)
        return rnn



class ClientSerializer(serializers.HyperlinkedModelSerializer):
    # menus = RNN_ClientMenuSerializer(source='rnn_clientmenu_set', many=True, read_only=False)

    class Meta:
        model = Client
        fields = ('url', 'id',
                  'name', 'location', ) # 'menus', )

    def create(self, validated_data):
        if 'name' in self.validated_data:
            client = Client.objects.create(name=validated_data['name'])
        else:
            # client = Client.objects.create(name=validated_data['name'], items=validated_data['menus'])
            client = Client.objects.create(name=validated_data['name'])
        return client

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    # items = RNN_MenuItemSerializer(source='rnn_menuitem_set', many=True, read_only=False)

    class Meta:
        model = Menu
        fields = ('url', 'id',
                  'name', )

    def create(self, validated_data):
        if 'name' not in self.validated_data:
            menu = Menu.objects.create(name=validated_data['name'])
        else:
            menu = Menu.objects.create(name=validated_data['name'])
            # menu = Menu.objects.create(name=name, items=items_list) #, item=item.id)

        return menu

class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('url', 'id',
                  'name')



class RNN_ShiftEmployeeSerializer(serializers.HyperlinkedModelSerializer):
    eqs = Employee.objects.all()
    sqs = Shift.objects.all()

    employee_id = serializers.PrimaryKeyRelatedField(many=False, queryset=eqs)
    shift_id = serializers.PrimaryKeyRelatedField(many=False, queryset=sqs)

    class Meta:
        model = RNN_ShiftEmployee
        fields = ('url', 'id',
                 'employee_id', 'shift_id', 'status', )

    def create(self, validated_data):
        employee_id = validated_data['employee_id'].id
        shift_id = validated_data['menu_id'].id

        employee = Employee.objects.get(pk=employee_id)
        shift = Shift.objects.get(pk=shift_id)
        status = validated_data['status']

        rnn = RNN_MenuItem.objects.create(employee=employee, shift=shift, status=status)
        return rnn


class ShiftSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Menu
        fields = ('url', 'id',
                  'name', )

    def create(self, validated_data):
        if 'name' not in self.validated_data:
            menu = Menu.objects.create(name=validated_data['name'])
        else:
            menu = Menu.objects.create(name=validated_data['name'])
            # menu = Menu.objects.create(name=name, items=items_list) #, item=item.id)

        return menu

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('url', 'id',
                  'name')