from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=250, blank=True)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
       return f"{self.first_name} {self.last_name}"