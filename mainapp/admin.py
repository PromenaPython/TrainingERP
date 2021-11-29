from django.contrib import admin

# Register your models here.
from mainapp.models import Employees, Departments

admin.site.register(Employees)
admin.site.register(Departments)
