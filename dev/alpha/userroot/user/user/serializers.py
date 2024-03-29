from rest_framework import serializers
from user.user.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', #'highlight', 'owner',
                  'name') # , 'code', 'linenos', 'language', 'style')
