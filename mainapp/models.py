import to as to
from django.db import models

# Create your models here.
class Employees(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.IntegerField(max_length=100,unique=True)
    employee_id=models.IntegerField(max_length=100,unique=True,primary_key=True)
    email = models.EmailField(max_length=100)


class Departments(models.Model):
    Employee=models.ForeignKey(Employees,on_delete=models.CASCADE)
    software=models.CharField(max_length=100)
    Marketing=models.CharField(max_length=100)
    sales=models.IntegerField(max_length=100)
    Design=models.CharField(max_length=100)
    production=models.CharField(max_length=100)

