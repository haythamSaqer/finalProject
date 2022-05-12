from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class Customer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    customerPhone = models.CharField(max_length=15, unique=True)
    customerEmail = models.EmailField(unique=True)
    isActive = models.BooleanField(default=True)
    userName = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName + " " + self.lastName


def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


post_save.connect(create_token, sender=User)


# class EmployeeCategory(models.Model):
#     category = models.CharField(max_length=100)
#     def __str__(self):
#         return self.category
#
#
# class JopType(models.Model):
#     Type = models.CharField(max_length=100, default='Full Time')
#
#     def __str__(self):
#         return self.Type
#
#
# class Employee(models.Model):
#     employeeID = models.CharField(primary_key=True, max_length=50, unique=True)
#     employeeName = models.CharField(max_length=50)
#     employeeUserName = models.ForeignKey(User, on_delete=models.CASCADE)
#     employeeCategory = models.ForeignKey(EmployeeCategory, on_delete=models.CASCADE)
#     employeeJopType = models.ForeignKey(JopType, on_delete=models.CASCADE)
#     IsActive = models.BooleanField(default=True)
#     IsSuperVisor = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.employeeName
#


#
# class MeetingType(models.Model):
#     type = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.type
#
#
# class MarketingMeeting(models.Model):
#     datetime = models.DateTimeField(auto_now=True)
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     type = models.ForeignKey(MeetingType, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=200)
#     notes = models.TextField()
#
#     def __str__(self):
#         return self.subject + " " + self.customer.__str__()

