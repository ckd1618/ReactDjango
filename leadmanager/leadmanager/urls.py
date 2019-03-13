from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #make sure your frontend loads before the leads
    path('', include('frontend.urls')),
    path('', include('leads.urls')),
]
