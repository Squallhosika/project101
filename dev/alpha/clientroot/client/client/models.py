from django.db import models

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('created',)

class Menu(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')

    items = models.ManyToManyField(Item, through='RNN_MenuItem', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)

class Client(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    location = models.IntegerField(default=0)

    menus = models.ManyToManyField(Menu, through='RNN_ClientMenu', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)


class RNN_MenuItem(models.Model):
    # created = models.DateTimeField(auto_now_add=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
    #status = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()

    class Meta:
        pass
        # ordering = ('created',)

    def __str__(self):
        return self.menu.name #+ '_' + self.item.name

class RNN_ClientMenu(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True)
    #status = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        pass
        #ordering = ('created',)

    def __str__(self):
        return self.client.name #+ '_' + self.item.name


### Another service?
class Employee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('created',)

class Shift(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')

    employees = models.ManyToManyField(Item, through='RNN_ShiftEmployee', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)


class RNN_ShiftEmployee(models.Model):
    # created = models.DateTimeField(auto_now_add=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=100, blank=True, default='')
    # price = models.IntegerField()

    class Meta:
        pass
        # ordering = ('created',)

    def __str__(self):
        return self.shift.name