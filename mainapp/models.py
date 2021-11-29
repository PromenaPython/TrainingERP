from django.db import models

# Create your models here.
# class Employees(models.Model):
#     first_name=models.CharField(max_length=100)
#
# class Department(models.Model):
#     software=models.CharField(max_length=100)


class Roles(models.Model):
    developer=models.CharField(max_length=100),
    desigener=models.CharField(max_length=100),
    manager=models.CharField(max_length=100),
    lead=models.CharField(max_length=100),
    architect=models.CharField(max_length=100),
    sales_manager=models.CharField(max_length=100),
    employee_id=models.ForeignKey(Employees, on_delete=models.CASCADE)
    # customer_id=models.ForeignKey(customer_management, on_delete=models.CASCADE)

class customer_management(models.Model):
    sales_manager=models.ForeignKey(Roles, on_delete=models.CASCADE),
    marketing=models.ForeignKey(Department, on_delete=models.CASCADE),
    first_name=models.CharField(max_length=100),
    last_name=models.CharField(max_length=100),
    business=models.CharField(max_length=100),
    contact_number=models.IntegerField(max_length=10),
    city=models.CharField(max_length=100),
    Email=models.EmailField(max_length=50)



