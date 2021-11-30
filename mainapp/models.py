# import to as to
from django.db import models

#Create your models here.
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


class Inventorymodel(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=40)

class Ordermodel(models.Model):
    oid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50)
    quantity = models.CharField(max_length=10)
    price = models.CharField(max_length=40)
    pid = models.ForeignKey(Inventorymodel, related_name="order", on_delete=models.CASCADE)
    # cid = models.ForeignKey(Inventorymodel, related_name="order", on_delete=models.CASCADE)
# class Employees(models.Model):
#     first_name=models.CharField(max_length=100)
#
# class Department(models.Model):
#     software=models.CharField(max_length=100)


class Roles(models.Model):
    developer=models.CharField(max_length=100)
    desigener=models.CharField(max_length=100)
    manager=models.CharField(max_length=100)
    lead=models.CharField(max_length=100)
    architect=models.CharField(max_length=100)
    sales_manager=models.CharField(max_length=100)
    employee_id=models.ForeignKey(Employees, on_delete=models.CASCADE)
    # customer_id=models.ForeignKey(customer_management,on_delete=models.CASCADE)

class customer_management(models.Model):
    sales_manager=models.ForeignKey(Roles, on_delete=models.CASCADE)
    marketing=models.ForeignKey(Departments, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    business=models.CharField(max_length=100)
    contact_number=models.IntegerField(max_length=10)
    city=models.CharField(max_length=100)
    Email=models.EmailField(max_length=50)



