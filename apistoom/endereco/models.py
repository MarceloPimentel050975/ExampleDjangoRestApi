# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Endereco(models.Model):

        streetName=models.CharField(max_length=200)
        number=models.CharField(max_length=10)
        complement=models.CharField(max_length=500)
        neighbourhood=models.CharField(max_length=300)
        city=models.CharField(max_length=300)
        state=models.CharField(max_length=200)
        country=models.CharField(max_length=200)
        zipcode=models.CharField(max_length=15)
        latitude=models.CharField(max_length=30)
        longitude=models.CharField(max_length=30)
    
        def __str__(self):
            return self.streetName