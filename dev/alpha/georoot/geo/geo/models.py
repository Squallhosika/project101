# from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import Distance

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    last_location = models.PointField(max_length=40, null=True)
    preferred_radius = models.IntegerField(default=5, help_text="in kilometers")

    objects = models.GeoManager()


class Client(models.Model):
    # created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    location = models.PointField(max_length=40, null=True)
    # client_id = models.IntegerField()

    objects = models.GeoManager()


