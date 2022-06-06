from django.urls import path
from .views import SubscriptionListView, SubscriptionDetailView, SubscriptionCreateView


urlpatterns = [
    path('<slug:slug>', SubscriptionDetailView.as_view(), name="subscription_detail"),
    path('new/', SubscriptionCreateView.as_view(), name="subscription_new"),
    path('', SubscriptionListView.as_view(), name='subscription_list'),
    
]