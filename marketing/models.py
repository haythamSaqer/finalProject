from django.db import models
from customer.models import Customer
from hr.models import Employee


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


class PriceOfferType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class PriceOffer(models.Model):
    priceOfferType = models.ForeignKey(PriceOfferType, on_delete=models.CASCADE)
    empID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=200)
    customerFullName = models.CharField(max_length=200)
    customerAddress = models.CharField(max_length=200)
    customerPhoneNumber = models.CharField(max_length=20)
    statement = models.TextField()
    priceInNumber = models.IntegerField()
    priceInLetters = models.CharField(max_length=200)
    totalArea = models.IntegerField()
    totalTimePeriod = models.IntegerField()

    def __str__(self):
        return self.customerFullName


class Component(models.Model):
    componentName = models.CharField(max_length=200)

    def __str__(self):
        return self.componentName


class ComponentType(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    componentTypeName = models.CharField(max_length=200)

    def __str__(self):
        return self.componentTypeName


class ComponentTypeItem(models.Model):
    component = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    componentTypeItem = models.CharField(max_length=200)

    def __str__(self):
        return self.componentTypeItem


class WorkingScope(models.Model):
    workingScope = models.CharField(max_length=200)

    def __str__(self):
        return self.workingScope


class WorkingScopeType(models.Model):
    component = models.ForeignKey(WorkingScope, on_delete=models.CASCADE)
    workingScopeTypeName = models.CharField(max_length=200)

    def __str__(self):
        return self.workingScopeTypeName


class WorkingScopeTypeItem(models.Model):
    component = models.ForeignKey(WorkingScopeType, on_delete=models.CASCADE)
    workingScopeTypeNameItem = models.CharField(max_length=200)

    def __str__(self):
        return self.workingScopeTypeNameItem


class ContractType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Contract(models.Model):
    contractType = models.ForeignKey(ContractType, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    priceInNumber = models.IntegerField()
    priceInLetters = models.CharField(max_length=200)
    totalArea = models.IntegerField()
    totalTimePeriod = models.IntegerField()
    GregorianDate = models.DateTimeField(auto_now_add=True)
    ContractCoverLetters = models.TextField()
    # component = models.ForeignKey(Component, on_delete=models.CASCADE)
    workingScope = models.TextField()
    additionalDetails = models.TextField()
    MunicipalConfirmed = models.BooleanField()
    adminApproval = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.firstName + " " + self.customer.lastName




"""
10)	Contract 
ID	Auto inc , primary key	
Contract_type	FK	
Customer_phone_number	string	
Project_name	Srting	
Customer_full_name	String	
CustomerAddress	String	
Price_in_letters	String	
Price_in_numbers	Number	
Total_area	Number	
Total_time_period	Number	
Gregorian_date	Date	
Hijri_date	Date	
Second_side	String	
Contract_cover_letters	Text area	
Project_components	Text area	
working_domain	Text area	
additional_details	Text area	
Municipal confirmed 	Boolean 	

"""

