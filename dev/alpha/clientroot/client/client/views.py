from rest_framework import viewsets
from client.client.serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.app.api.base import call_function


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class RNN_ClientMenuViewSet(viewsets.ModelViewSet):
    queryset = RNN_ClientMenu.objects.all()
    serializer_class = RNN_ClientMenuSerializer

class RNN_MenuItemViewSet(viewsets.ModelViewSet):
    queryset = RNN_MenuItem.objects.all()
    serializer_class = RNN_MenuItemSerializer


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class RNN_ShiftEmployeeViewSet(viewsets.ModelViewSet):
    queryset = RNN_ShiftEmployee.objects.all()
    serializer_class = RNN_ShiftEmployeeSerializer

class RNN_ClientShiftViewSet(viewsets.ModelViewSet):
    queryset = RNN_ClientShift.objects.all()
    serializer_class = RNN_ClientShiftSerializer



@api_view(['GET'])
def client_around(request):
    try:
        close_clients = Client.objects.filter(location=1)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(close_clients, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_active_menu(request):
    try:
        client_id = request.data.get('client_id')
        active_menu = RNN_ClientMenu.objects.filter(client_id=client_id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RNN_ClientMenuSerializer(active_menu, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_employees_by_client_status(request):
    try:
        client_id = request.data.get('client_id')
        status = request.data.get('status')
        employees = Employee.objects.filter(client_id=client_id, status=status)

    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employees, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_shifts_by_client_status(request):
    try:
        client_id = request.data.get('client_id')
        status_shift = request.data.get('status')

        if status_shift == 'all':
            shifts = Shift.objects.filter(client_id=client_id)
        else:
            shifts = Shift.objects.filter(client_id=client_id, status=status_shift)

    except Shift.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShiftSerializer(shifts, context={'request': request}, many=True)
        return Response(serializer.data)



@api_view(['PUT'])
def shift_activate(request):
    try:
        pk = request.data.get('id')
        shift = Shift.objects.get(pk=pk)
    except Shift.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ShiftSerializer(shift, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid() and request.data['status'] == 'active':
            param = {'master_id', shift.id}
            # create a queue when activate the shift
            req_createqueue = call_function('POST', 'dqueue', 'createqueue', param)
            if not req_createqueue.status_code == status.HTTP_201_CREATED:
                return req_createqueue

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def shift_desactivate(request):
    try:
        pk = request.data.get('id')
        shift = Shift.objects.get(pk=pk)
    except Shift.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ShiftSerializer(shift, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid() and request.data['status'] == 'inactive':
            param = {'master_id', shift.id}
            # create a queue when activate the shift
            call_function('GET', 'dqueue', 'deletequeue', param)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def create_client(request):
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_menu(request):
    if request.method == 'POST':
        serializer = MenuSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_item(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_shift(request):
    if request.method == 'POST':
        serializer = ShiftSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update_client(request):
    try:
        pk = request.data.get('id')
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_menu(request):
    try:
        pk = request.data.get('id')
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = MenuSerializer(menu, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_item(request):
    try:
        id = request.data.get('id')
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_shift(request):
    try:
        id = request.data.get('id')
        shift = Shift.objects.get(pk=id)
    except Shift.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ItemSerializer(shift, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_employee(request):
    try:
        id = request.data.get('id')
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ItemSerializer(employee, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_client(request):
    try:
        pk = request.data.get('id')
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_menu(request):
    try:
        pk = request.data.get('id')
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_item(request):
    try:
        id = request.data.get('id')
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_shift(request):
    try:
        id = request.data.get('id')
        shift = Shift.objects.get(pk=id)
    except Shift.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        shift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_employee(request):
    try:
        id = request.data.get('id')
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def add_menu_to_client(request):
    if request.method == 'POST':
        # return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = RNN_ClientMenuSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_item_to_menu(request):
    if request.method == 'POST':
        # return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = RNN_MenuItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_employee_to_shift(request):
    if request.method == 'POST':
        # return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = RNN_ShiftEmployeeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_menus_from_client(request):
    try:
        client_id = request.data.get('client_id')
        client_menu = RNN_ClientMenu.objects.filter(client_id=client_id)
    except RNN_ClientMenu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RNN_ClientMenuSerializer(client_menu, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_items_from_menu(request):
    try:
        menu_id = request.data.get('menu_id')
        menu_item = RNN_MenuItem.objects.filter(menu_id=menu_id)
    except RNN_MenuItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RNN_MenuItemSerializer(menu_item, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_employees_from_shift(request):
    try:
        shift_id = request.data.get('shift_id')
        shift_employee = RNN_ShiftEmployee.objects.filter(shift_id=shift_id)
    except RNN_ShiftEmployee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        employee_ids = [employee.employee_id for employee in shift_employee]
        qs_e = Employee.objects.filter(id=employee_ids[0])
        qss = [Employee.objects.filter(id=id) for id in employee_ids[1:]]
        qs_e = qs_e.union(*qss)
        serializer = EmployeeSerializer(qs_e, context={'request': request}, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
def remove_menu_from_client(request):
    try:
        pk = request.data.get('id')
        client_menu = RNN_ClientMenu.objects.get(pk=pk)
    except RNN_ClientMenu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        client_menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def remove_item_from_menu(request):
    try:
        menu_id = request.data.get('menu_id')
        item_id = request.data.get('item_id')
        menu_item = RNN_MenuItem.objects.get(item_id=item_id, menu_id=menu_id)
    except RNN_MenuItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        menu_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def remove_employee_from_shift(request):

    if 'id' in request.data:
        return remove_employee_from_shift_by_id(request)
    else:
        return remove_employee_from_shift_by_shift_employee(request)


def remove_employee_from_shift_by_id(request):
    try:
        pk = request.data.get('id')
        shift_employee = RNN_ShiftEmployee.objects.get(pk=pk)
    except RNN_ShiftEmployee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        shift_employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def remove_employee_from_shift_by_shift_employee(request):
    try:
        shift_id = request.data.get('shift_id')
        employee_id = request.data.get('employee_id')
        shift = Shift.objects.get(id=shift_id)
        employee = Employee.objects.get(id=employee_id)
        shift_employees = RNN_ShiftEmployee.objects.filter(shift=shift, employee=employee)
    except RNN_ShiftEmployee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        [se.delete() for se in shift_employees]
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)
