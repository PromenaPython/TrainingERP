"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainapp import views
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="inventory",
        default_version="v1",
        description="inventory description",
        terms_of_service="https://www.promena.net/en",
        contact=openapi.Contact(email="promena@gmail.com"),
        license=openapi.License(name="Promena License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register("Inventorymodel", views.Inventoryapi)
router.register("Ordermodel", views.Orderapi)
router.register("Employees", views.Employeesapi)
router.register("Departments", views.Departmentsapi)
router.register("Roles", views.Rolesapi)
router.register("customer_management", views.customer_managementapi)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("Inventorymodel", views.Inventoryapi)
    # path("Ordermodel", views.Orderapi)
    path('', include(router.urls)),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0)),
    path('swagger-docs', schema_view.with_ui('redoc', cache_timeout=0))

]


