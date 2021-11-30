from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class Inventoryapi(viewsets.ModelViewSet):
    queryset = Inventorymodel.objects.all()
    serializer_class = InventorySerializer

class Orderapi(viewsets.ModelViewSet):
    queryset = Ordermodel.objects.all()
    serializer_class = OrderSerializer

class Employeesapi(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class Departmentsapi(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class Rolesapi(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class customer_managementapi(viewsets.ModelViewSet):
    queryset = customer_management.objects.all()
    serializer_class = customer_managementSerializer



