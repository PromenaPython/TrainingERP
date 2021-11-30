from rest_framework import serializers

from mainapp.models import Roles,customer_management

class rolesSerializers(serializers.ModelSerializer):
    class Meta():
        model=Roles
        fields='__all__'

class Customer_managementSerializers(serializers.ModelSerializer):
    class Meta():
        model=customer_management
        fields='__all__'