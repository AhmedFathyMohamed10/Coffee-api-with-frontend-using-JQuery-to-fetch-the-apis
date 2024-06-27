from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Coffee, CoffeeImageModel
from .serializers import CoffeeImageSerializer, CoffeeSerializer

class CoffeeList(generics.ListCreateAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

class CoffeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Coffee, slug=slug)

class CoffeeImageCreate(generics.CreateAPIView):
    queryset = CoffeeImageModel.objects.all()
    serializer_class = CoffeeImageSerializer

def index(request):
    return render(request, 'coffees.html')

def coffee_detail(request, slug):
    coffee = get_object_or_404(Coffee, slug=slug)
    # Set is_available based on the stock value
    coffee.is_available = coffee.stock > 0
    return render(request, 'coffee_details.html', {'coffee': coffee})