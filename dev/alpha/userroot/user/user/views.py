from rest_framework import viewsets
from user.user.serializers import *

from rest_framework import status
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def get_client_around_me(request, position):
    """
    Belong to client
    :return:
    """
    if request.method == 'GET':
        return

def get_client_by_name(): pass

def get_client_menu(): pass

def get_estimated_time(): pass

def create_order(): pass

def update_order(): pass

def cancel_order(): pass

def get_queue_position(): pass

def create_profile(): pass

def update_profile(): pass

def create_payement_details(): pass

def update_payement_details(): pass

def select_payement_method(): pass

def update_work_flow(): pass

def rating_client(): pass