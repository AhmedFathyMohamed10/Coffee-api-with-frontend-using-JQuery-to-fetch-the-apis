from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Coffee
from .serializers import CoffeeSerializer

class CoffeeList(generics.ListCreateAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

class CoffeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

def index(request):
    return render(request, 'coffees.html')

def coffee_detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, 'coffee_details.html', {'coffee': coffee})