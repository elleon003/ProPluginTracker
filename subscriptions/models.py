from django.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField
from dateutil.relativedelta import relativedelta
from autoslug import AutoSlugField


class Subscription(models.Model):
    name = models.CharField(max_length=150, db_column="subscription_name", unique=True)
    website = models.URLField(db_column="subscription_website", unique=False)
    purchase_date = models.DateField()
    amount = MoneyField(max_digits=19, decimal_places=2, default_currency='USD', db_column='renewal_amount')
    related_contact = models.ForeignKey('contacts.Contact', on_delete=models.CASCADE, null=True, blank=True)
    slug = AutoSlugField(populate_from='name', null=True, unique=True)

    def __str__(self):
        return self.name
    
    @property
    def due_date(self):
        due_date = self.purchase_date + relativedelta(years=1)
        return due_date

    def get_absolute_url(self):
        return reverse("subscription_detail", args=[str(self.slug)])
    


