from django.urls import path
from cars_project.cars_auth import views

urlpatterns = (
    path('login/', views.cars_login, name='login'),
    path('register/', views.cars_register, name='register'),
    path('logout/', views.cars_logout, name='logout'),
)