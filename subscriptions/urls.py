from django.urls import path
from .views import SubscriptionListView, SubscriptionDetailView


urlpatterns = [
    path('', SubscriptionListView.as_view(), name='subscription_list'),
    path('<slug:slug>', SubscriptionDetailView.as_view(), name="subscription_detail"),
    
]