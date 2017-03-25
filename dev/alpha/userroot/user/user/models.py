from django.db import models


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)


class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=250, blank=True, default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)
