from rest_framework import serializers
from .models import *


class DesignTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignType
        fields = '__all__'


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ItemsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsTable
        fields = '__all__'


class MoodBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodBoard
        fields = '__all__'


class StyleMoodBoardPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = StyleMoodBoardPart
        fields = '__all__'


class MoodBoardPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodBoardPart
        fields = '__all__'


class MoodBoardPartImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodBoardPartImages
        fields = '__all__'


class ProjectTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTasks
        fields = '__all__'
