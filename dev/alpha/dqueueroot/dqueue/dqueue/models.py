from django.db import models

# Create your models here.


class Queue(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    master_id = models.IntegerField() # in this case shift_id
    type = models.CharField(max_length=100, blank=True, default='')
    node_id_first = models.IntegerField(blank=True, null=True)
    node_id_last = models.IntegerField(blank=True, null=True)


class Node(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id_previous = models.IntegerField(blank=True, null=True)
    id_next = models.IntegerField(blank=True, null=True)
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)
    time = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
