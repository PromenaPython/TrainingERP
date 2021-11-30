from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordermodel
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    orders = OrderSerializer(read_only=True, many=True)
    class Meta:
        model = Inventorymodel
        fields = '__all__'

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    departments = DepartmentsSerializer(read_only=True, many=True)
    class Meta:
        model = Employees
        fields = '__all__'

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"

class customer_managementSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer_management
        fields = "__all__"

