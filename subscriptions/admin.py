from django.contrib import admin
from subscriptions.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_display = ('name', 'due_date', 'amount')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Subscription, SubscriptionAdmin)
