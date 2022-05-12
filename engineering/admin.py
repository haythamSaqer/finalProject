from django.contrib import admin
from .models import DesignType, ProjectType, Project, ItemsTable, MoodBoard, StyleMoodBoardPart, MoodBoardPart, MoodBoardPartImages
# Register your models here.


admin.site.register([DesignType, ProjectType, Project, ItemsTable, MoodBoard, StyleMoodBoardPart, MoodBoardPart, MoodBoardPartImages])


