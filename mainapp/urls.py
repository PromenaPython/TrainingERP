from django.urls import path,include
from rest_framework.routers import DefaultRouter

from mainapp import views
from mainapp.views import Employee,Departments
# router = DefaultRouter()
# router.register("Employee", views.Employee)
# router.register("Departments", views.Depart)

urlpatterns = [
    path('',Employee),
]
