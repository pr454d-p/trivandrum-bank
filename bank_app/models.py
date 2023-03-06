from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class District(models.Model):
    district = models.CharField(max_length=250)

    def __str__(self):
        return self.district

    
class Branches(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    branch = models.CharField(max_length=250)
    wiki = models.TextField()

    def __str__(self):
        return self.branch

class Account(models.Model):
    account = models.CharField(max_length=250)

    def __str__(self):
        return self.account

class Details(models.Model):
    name = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    phone_number = PhoneNumberField(blank=True,unique=True)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branches, on_delete=models.SET_NULL, blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    cheque_book = models.BooleanField()
    credit_card = models.BooleanField()
    debit_card = models.BooleanField()
    passbook = models.BooleanField()
    
    def __str__(self):
        return self.name