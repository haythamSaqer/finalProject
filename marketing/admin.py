from django.contrib import admin
from .models import MarketingMeeting, MeetingType, Customer


admin.site.register([MarketingMeeting, MeetingType])
