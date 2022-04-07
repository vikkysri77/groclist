from django.db import models

import datetime

from django.contrib.auth.models import User

from django.utils import timezone


class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.CharField(max_length=100, blank=True)
    interested = models.PositiveIntegerField(default=0)

    def __str__(Item):
        return Item.name

    def topup(self):
        self.stock += 200
        return Item.stock

class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'WATERLOO'), ]
    # fullname = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone_number = models.IntegerField(blank=True, null=True)

    # is_active =
    def __str__(self):
        return self.first_name + '' + self.last_name


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    itemsCount = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = (('0', 'cancelled Order'), ('1', 'placed order'), ('2', 'shipped order'), ('3', 'delivered order'))
    status_options = models.CharField(max_length=1, choices=STATUS_CHOICES)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'OrderItemClass(item=' + str(self.item) + ' ,client=' + str(self.client) + ',itemsCount=' + str(
            self.itemsCount) \
               + ',status = ' + str(self.status_options) + ',updatedDate = ' + str(self.updatedDate) + ')'

    def total_price(self):
        return self.itemsCount * self.item.price
