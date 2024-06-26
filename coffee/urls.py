from django.urls import path
from .views import CoffeeList, CoffeeDetail

urlpatterns = [
    path('coffees/', CoffeeList.as_view(), name='coffee-list'),
    path('coffees/<int:pk>/', CoffeeDetail.as_view(), name='coffee-detail'),
]
