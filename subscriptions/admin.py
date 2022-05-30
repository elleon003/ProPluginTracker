from django.contrib import admin
from subscriptions.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_display = ('subscription_name',)
    prepopulated_fields = {'slug': ('subscription_name',)}

admin.site.register(Subscription, SubscriptionAdmin)
