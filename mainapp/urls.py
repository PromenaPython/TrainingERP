from django.urls import path

from mainapp import views

urlpatterns = [
    path('', views.Employee),
    # path('mainapp',include('mainapp.urls'))
]
