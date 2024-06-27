from django.urls import path
from .views import CoffeeList, CoffeeDetail, CoffeeImageCreate

urlpatterns = [
    path('coffees/', CoffeeList.as_view(), name='coffee-list'),
    path('coffees/<int:pk>/', CoffeeDetail.as_view(), name='coffee-detail'),
    path('coffees/image-create/', CoffeeImageCreate.as_view(), name='coffee-image-create'),
]
