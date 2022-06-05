from ast import Sub
from django.shortcuts import render
from subscriptions.models import Subscription

def index(request):
    return render(request, 'home.html')