from django.urls import path
from .views import DriverListCreateView

urlpatterns = [
    path('drivers/', DriverListCreateView.as_view(), name='driver-list-create'),
]
