from django.db import models


class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    item_id = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, blank=True, default='created')

    client_id = models.IntegerField()
    menu_id = models.IntegerField()
    user_id = models.IntegerField()

    items = models.ManyToManyField(Item, through='RNN_OrderItem', blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('created',)

# TODO we assume only one queue by client find a clean way to insure that
class Queue(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    current_rank = models.IntegerField(default=-1)
    last_rank = models.IntegerField(default=-1)

    client_id = models.IntegerField(default=0)
    # position = models.IntegerField(default=-1)

    orders = models.ManyToManyField(Order, through='RNN_QueueOrder', blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('created',)



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

class RNN_QueueOrder(models.Model):
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)

    order_rank = models.IntegerField(default=0)
    # order_status = models.CharField(max_length=100, blank=True, default='created')
    employee_id = models.IntegerField(default=0)


    class Meta:
        pass

    def __str__(self):
        return self.queue.id #+ '_' + self.item.name



# class OrderFlow(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     client_id = models.IntegerField()
#     employee_id = models.IntegerField(default=-1)
#     status = models.CharField(max_length=100, blank=True, default='')
#     rank = models.IntegerField(default=-1)
#
#     def __str__(self):
#         return str(self.id)

