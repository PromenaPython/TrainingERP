from django.db import models

# Create your models here.

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