from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, 'index.html', {})

# class bookingView(APIView):
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})
        
class MenuItemView(ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class BookingView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer