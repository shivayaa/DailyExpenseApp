from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Income(models.Model):
    income=models.IntegerField()
    incomeType=models.CharField(max_length=300)
    incomeDate=models.DateField()
    discription=models.TextField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='income'

class Expense(models.Model):
    expense=models.IntegerField()
    expenseType=models.CharField(max_length=300)
    expenseDate=models.DateField()
    discription=models.TextField(max_length=300)
    User=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='expense' 
