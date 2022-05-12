from django.urls import path
from . import views
from engineering.views import projectViews

urlpatterns = [

    path('project/', projectViews.ProjectList.as_view()),
    path('projectList/<int:pk>/', projectViews.Project.as_view()),
    # path('meetingTypeList/', views.MeetingTypeList.as_view()),

]
