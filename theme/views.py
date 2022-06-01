from ast import Sub
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from subscriptions.models import Subscription

def index(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'home.html', {
        'subscriptions':subscriptions,
    })