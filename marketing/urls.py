from django.urls import path
from . import views

urlpatterns = [

    path('meetingList/', views.MeetingList.as_view()),
    path('meetingType/<int:pk>/', views.MeetingTypeDD.as_view()),
    path('meetingTypeList/', views.MeetingTypeList.as_view()),

]
