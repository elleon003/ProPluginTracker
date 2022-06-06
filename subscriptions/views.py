from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from subscriptions.models import Subscription

class SubscriptionListView(ListView):
    model = Subscription
    template_name = "subscriptions/subscription_list.html"
    extra_context={'subscriptions': Subscription.objects.all()}

class SubscriptionDetailView(DetailView):
    model = Subscription
    template_name = "subscriptions/subscription_detail.html"

class SubscriptionCreateView(CreateView):
    model = Subscription
    template_name = "subscriptions/subscription_new.html"
    fields = ["name", "website", "purchase_date", "amount",]