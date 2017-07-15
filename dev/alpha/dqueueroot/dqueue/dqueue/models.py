from django.db import models

# Create your models here.


class Queue(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    shift_id = models.IntegerField()
    node_id_first = models.IntegerField(blank=True, null=True)
    node_id_last = models.IntegerField(blank=True, null=True)


class Node(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id_previous = models.IntegerField()
    id_next = models.IntegerField()
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)
    time = models.DecimalField()