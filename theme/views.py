from django.shortcuts import render

def index(request):
    dashboard = "This is going to be a dashboard"
    return render(request, 'home.html', {
        'dashboard':dashboard,
    })