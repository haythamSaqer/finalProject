from django.contrib import admin
from .models import Customer, JopType, EmployeeCategory, Employee


admin.site.register([Customer, JopType, EmployeeCategory, Employee])
