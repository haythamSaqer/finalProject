from django.contrib import admin
from .models import MarketingMeeting, MeetingType, Contract, ContractType, ComponentType


admin.site.register([MarketingMeeting, MeetingType, ComponentType, Contract, ContractType])
