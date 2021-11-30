from django.http import HttpResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
# Create your views here.
# def home():
#     pass
# def Employee(request):
#     return HttpResponse("hello")
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# from rest_framework.views import APIView
#
#
from mainapp.serializers import rolesSerializers
#
#

class roles(GenericAPIView):
    # @swagger_auto_schema()
    # @swagger_auto_schema(method='post', operation_description="POST")
    serializer_class = rolesSerializers
    def post(self,request):
        serializer=rolesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        data=rolesSerializers.objects.all()
        serializer=self.serializer_class(data,many=True)
        serialized_data=serializer
        return Response(serialized_data,status=status.HTTP_200_OK)


    # def post(self,request):



