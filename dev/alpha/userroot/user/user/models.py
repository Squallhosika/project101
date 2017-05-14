from django.db import models

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')

    #menus = models.ManyToManyField(Menu, through='RNN_ClientMenu', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)
