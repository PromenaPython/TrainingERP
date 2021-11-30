from django.urls import path,include
from rest_framework.routers import DefaultRouter

from mainapp.models import Roles
# from mainapp.views import home, Employee
from mainapp.views import roles
router = DefaultRouter()

urlpatterns = [
    path('',roles.as_view()),
]
