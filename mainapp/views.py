from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from requests import Response
from rest_framework.generics import GenericAPIView
from rest_framework import serializers, status
from rest_framework.views import APIView

from .serializers import *
from rest_framework import views,generics,viewsets


# Create your views here.
# class Employee(GenericAPIView):
#     serializer_class = Empserializer
#     def post(self,request):
#         serializer=Empserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self,request):
#         quary=Empserializer.objects.all()
#         serializer=Empserializer(quary)
#         return Response(serializer.data)


from django.shortcuts import render
from .models import *
from .serializers import Empserializer, Depserializer
from rest_framework import viewsets
# from drf_yasg.utils import swagger_auto_schema
class Employee(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = Empserializer

class Depart(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = Depserializer





