from django.contrib import admin
from .models import Department, Engineer, EmployeeCategory, JopType, Employee


admin.site.register([Department, Engineer, EmployeeCategory, JopType, Employee])
