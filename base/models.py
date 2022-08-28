from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

   
    


    def __str__(self):
        return self.name

class Prize(models.Model):

    name = models.CharField(max_length=200, null=True)
    value = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)

   
    

    def __str__(self):
        return self.name


class Payment(models.Model):


    Payment = models.CharField(max_length=200, null=True)


   
    


    def __str__(self):
        return self.paynment

class Raffle(models.Model):

    name = models.CharField(max_length=200, null=True)

   
    


    def __str__(self):
        return self.name

