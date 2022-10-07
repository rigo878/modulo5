from pyexpat import model
from turtle import update
from django.db import models


class Sender(models.Model):
    fullName=models.CharField(max_length=200,unique=True) 
    ciNit=models.CharField(max_length=10,unique=True)
    phoneNumber=models.CharField(max_length=12)
    email=models.EmailField(max_length=250)
     
    def __str__(self):
        return self.fullName

class Receiver(models.Model):
    fullName=models.CharField(max_length=200,unique=True)
    ciNit=models.CharField(max_length=10,unique=True)
    phoneNumber=models.CharField(max_length=12)
    email=models.EmailField(max_length=250)

class Address(models.Model):
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    latitude=models.CharField(max_length=30)
    longitude=models.CharField(max_length=30)

class Packet(models.Model):
    type=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=10)
    sender=models.ForeignKey(Sender, on_delete=models.CASCADE)
    receiver=models.ForeignKey(Receiver, on_delete=models.CASCADE)
    address=models.ForeignKey(Address, on_delete=models.CASCADE)

class TypeService(models.TextChoices):
    STANDARD='s','Standard'
    PREMIUM='p','premium'

class Service(models.Model):
    type=models.CharField(
        max_length=2,
        choices=TypeService.choices,
        default=TypeService.STANDARD
    )
class TypeStatus(models.TextChoices):
    DELIVERED='Entregado','Entregado'
    WAREHOUSE='Almacen','Almacen'
    ONWAY='Encamino', 'En camino'

class Status(models.Model):
    type=models.CharField(
        max_length=10,
        choices=TypeStatus.choices,
        default=TypeStatus.DELIVERED
    )
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    service=models.ForeignKey(Service, on_delete=models.CASCADE)
    packet=models.ForeignKey(Packet, on_delete=models.CASCADE)
