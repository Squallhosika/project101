from django.db import models

# Create your models here.
class Client(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    #code = models.TextField()
    #linenos = models.BooleanField(default=False)
    #language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    #style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

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
    # items = models.CharField(max_length=100, blank=True, default='item42')
    items = models.ManyToManyField(Item, through='RNN_MenuItem')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)

class RNN_MenuItem(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    #status = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()

    class Meta:
        pass
        #ordering = ('created',)

    def __str__(self):
        return self.menu.name + '_' + self.item.name

