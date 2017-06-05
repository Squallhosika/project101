from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from geo.geo.models import *

class UserSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = User
        geo_field = "last_location"
        fields = ('url', 'id', 'name', 'preferred_radius')

class UserSerializer2(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'name', 'last_location', 'preferred_radius')

class ClientSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Client
        geo_field = "location"
        fields = ('url', 'id', 'name')
