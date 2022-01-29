from django.urls import path
from cars_project.cars import views

urlpatterns = (
    path('add-car/', views.add_car, name='add car'),
    path('', views.list_cars, name='list cars'),
    path('<int:pk>/', views.car_details, name='car details'),
    path('edit_car/<int:pk>/', views.edit_car, name='car edit'),
    path('delete_car/<int:pk>/', views.delete_car, name='car delete'),
    path('like/<int:pk>/', views.like_car, name='like car'),
)