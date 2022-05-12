from django.contrib import admin
from django.urls import path, include
from marketing.views import approve_contract

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('customer/', include('customer.urls')),
    path('marketing/', include('marketing.urls')),
    path('engineering/', include('engineering.urls')),
    path('admin-approve-contract/<int:pk>/', approve_contract)

]
