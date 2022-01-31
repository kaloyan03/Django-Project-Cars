from django.urls import path
from cars_project.cars_rent_car import views


urlpatterns = [
    path('<int:pk>', views.rent_car, name='rent car'),
    path('rent/', views.rent_cart, name='rent cart')
]