from .views import *
from django.urls import path

urlpatterns = [
   path('', index, name='index'),
   path('menu/', MenuItemView.as_view(), name='menu'),
   path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu'),
   path('booking/', BookingView.as_view(), name='booking'),
   path('booking/<int:pk>/', SingleBookingView.as_view(), name='single-booking'),
   
]
