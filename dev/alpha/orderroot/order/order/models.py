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
    items = models.ManyToManyField(Item, through='RNN_OrderItem', blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('created',)


class OrderFlow(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    client_id = models.IntegerField()
    employee_id = models.IntegerField(default=-1)
    status = models.CharField(max_length=100, blank=True, default='')
    rank = models.IntegerField(default=-1)

    def __str__(self):
        return str(self.id)


# TODO we assume only on queue by client find a clean way to insure that
class Queue(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    client_id = models.IntegerField()
    position = models.IntegerField(default=-1)
    last_rank = models.IntegerField(default=-1)

    def __str__(self):
        return str(self.id)


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
