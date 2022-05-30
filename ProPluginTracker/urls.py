from django.contrib import admin
from django.urls import include, path

from theme import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subscriptions/', include('subscriptions.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
