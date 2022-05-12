from django.db import models
from marketing.models import Contract

from customer.models import Customer


class DesignType(models.Model):
    type = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.type


class ProjectType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Project(models.Model):
    """

    """
    projectType = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=3)
    numberOfWindows = models.IntegerField()
    projectIssueDate = models.DateField()  # starting date for the project
    projectDueDate = models.DateField()
    municipalConfirmed = models.BooleanField()
    customerFinishingConfirm = models.BooleanField(default=False)
    customerNotes = models.TextField()
    currentProgress = models.FloatField()

    def __str__(self):
        return self.contract.__str__()


class ItemsTable(models.Model):
    itemName = models.CharField(max_length=50)
    creationTime = models.FloatField()
    modificationTime = models.FloatField()

    def __str__(self):
        return self.itemName


class MoodBoard(models.Model):
    type = models.ForeignKey(DesignType, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    notes = models.TextField(max_length=200)

    def __str__(self):
        return self.type.__str__()


class StyleMoodBoardPart(models.Model):
    styleType = models.CharField(max_length=50)

    def __str__(self):
        return self.styleType


class MoodBoardPart(models.Model):
    tableItem = models.ForeignKey(ItemsTable, on_delete=models.CASCADE)
    moodBoardParent = models.ForeignKey(MoodBoard, on_delete=models.CASCADE)
    style = models.ForeignKey(StyleMoodBoardPart, on_delete=models.CASCADE)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.notes


class MoodBoardPartImages(models.Model):
    part = models.ForeignKey(MoodBoardPart, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to="images")
    imageNote = models.CharField(max_length=200)

    def __str__(self):
        return self.imageNote