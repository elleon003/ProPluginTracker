from django.views.generic import ListView, DetailView

from subscriptions.models import Subscription

class SubscriptionListView(ListView):
    model = Subscription
    template_name = "subscriptions/subscription_list.html"
    extra_context={'subscriptions': Subscription.objects.all()}

class SubscriptionDetailView(DetailView):
    model = Subscription
    template_name = "subscriptions/subscription_detail.html"