from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from .forms import BookingForm
from datetime import datetime
import json

from .serializers import MenuSerializer
from .models import Menu

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet): 
    permission_classes = [IsAuthenticated] 
    queryset = Menu.objects.all()





def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
         form = BookingForm(request.POST)
         if form.is_valid():
             form.save()
    context = {'form':form}
    return render(request, 'book.html', context)
    
def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})