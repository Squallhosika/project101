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
    shift_id = models.IntegerField()
    menu_id = models.IntegerField()
    user_id = models.IntegerField()
    ini_waiting_time = models.IntegerField(default=0) #  models.DecimalField(default=0, max_digits=20, decimal_places=10)

    items = models.ManyToManyField(Item, through='RNN_OrderItem', blank=True)

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
