from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=250)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)
