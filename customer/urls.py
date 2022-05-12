from django.urls import path
from . import views

urlpatterns = [
    path('customerList/', views.CustomerList.as_view()),
    path('customerList/<int:pk>', views.CustomerDetail.as_view()),
]
