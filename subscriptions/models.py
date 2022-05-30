from django.db import models
from djmoney.models.fields import MoneyField


class Subscription(models.Model):
    subscription_name = models.CharField(max_length=150)
    subscription_website = models.URLField()
    purchase_date = models.DateField()
    renewal_amount = MoneyField(max_digits=19, decimal_places=2, default_currency='USD')
    related_contact = models.ForeignKey('contacts.Contact', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.subscription_name
    


