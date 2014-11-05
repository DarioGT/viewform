from django.db import models


CITY_CHOICES = (('Paris', 'Paris'),
                ('London', 'London'),
                ('New York', 'New York'))


class Shipment(models.Model):
    name = models.CharField(max_length=150)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    city = models.CharField(choices=CITY_CHOICES, max_length=50)


class ShipmentItem(models.Model):
    shipment = models.ForeignKey(Shipment)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
