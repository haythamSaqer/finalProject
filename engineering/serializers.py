from rest_framework import serializers
from .models import *


class DesignTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignType
        fields = '_all_'


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = '_all_'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '_all_'


class ItemsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsTable
        fields = '_all_'


class MoodBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodBoard
        fields = '_all_'


class StyleMoodBoardPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = StyleMoodBoardPart
        fields = '_all_'


class MoodBoardPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodBoardPart
        fields = '_all_'


class MoodBoardPartImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodBoardPartImages
        fields = '_all_'
