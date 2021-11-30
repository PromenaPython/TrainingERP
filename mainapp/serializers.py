from rest_framework import serializers
from .models import Employees, Departments


class Empserializer(serializers.ModelSerializer):
    class Meta():
        model = Employees
        fields = ["first_name","last_name","contact_number","employee_id","email"]


class Depserializer(serializers.ModelSerializer):
    class Meta():
        model = Departments
        fields = "__all__"

