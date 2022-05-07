from rest_framework import serializers
from .models import MarketingMeeting, MeetingType


class MarketingMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingMeeting
        fields = '__all__'


class MeetingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingType
        fields = '__all__'
