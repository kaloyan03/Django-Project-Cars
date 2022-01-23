from django.urls import path
from cars_project.cars import views

urlpatterns = (
    path('add-car/', views.add_car, name='add car'),
    path('cars/', views.list_cars, name='list cars'),
)