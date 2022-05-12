from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Engineer(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField()

    def __str__(self):
        return self.name


class EmployeeCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class JopType(models.Model):
    Type = models.CharField(max_length=100, default='Full Time')

    def __str__(self):
        return self.Type


class Employee(models.Model):
    employeeID = models.CharField(primary_key=True, max_length=50, unique=True)
    employeeName = models.CharField(max_length=50)
    employeeUserName = models.ForeignKey(User, on_delete=models.CASCADE)
    employeeCategory = models.ForeignKey(EmployeeCategory, on_delete=models.CASCADE)
    employeeJopType = models.ForeignKey(JopType, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)
    IsSuperVisor = models.BooleanField(default=False)

    def __str__(self):
        return self.employeeName
