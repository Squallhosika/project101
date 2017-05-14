from django.db import models


class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    client_id = models.IntegerField()
    user_id = models.IntegerField()
    status = models.CharField(max_length=100, blank=True, default='')
    items = models.ManyToManyField(Item, through='RNN_OrderItem', blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('created',)

class Queue(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    client_id = models.IntegerField()
    status = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return str(self.id)


class OrderInQueue(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # TODO change Foreign to OneToOneField or put primary_key = true on ForeignKey Order
    # order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)
    position = models.IntegerField(default=-1)

class RNN_OrderItem(models.Model):
    # TODO order X item should be a primary key it is not the case today
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.order.id)
