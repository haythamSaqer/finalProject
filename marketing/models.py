from django.db import models
from customers.models import Customer, Employee


class MeetingType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class MarketingMeeting(models.Model):
    CHOICES = [
        ('C', 'Canceled'),
        ('D', 'Done'),
        ('P', 'Pending'),
        ('S', 'Shifted'),

    ]
    datetime = models.DateTimeField(auto_now=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.ForeignKey(MeetingType, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    notes = models.TextField()
    status = models.CharField(choices=CHOICES, max_length=40)

    def __str__(self):
        return self.subject + " " + self.customer.__str__()


