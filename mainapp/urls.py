from django.urls import path,include

from mainapp.views import home

urlpatterns = [
    path('',home),
]
