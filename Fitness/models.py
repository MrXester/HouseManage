from django.db import models
from colorfield.fields import ColorField
from django_cryptography.fields import encrypt
import json



class Metric(models.Model):
    food = models.BooleanField()
    name = models.CharField(max_length=20)
    color = ColorField(default='#FF0000')


class EncryptedTable(models.Model):
    metricRef = models.ForeignKey(Metric, on_delete=models.SET_NULL, null=True)
    encryptedData = models.BinaryField()
    dateRegister = models.DateField()
    dateEffect = models.DateField()
    value = encrypt(models.FloatField(default=0.0))


