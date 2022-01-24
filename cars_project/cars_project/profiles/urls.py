from django.urls import path

from cars_project.profiles import views

urlpatterns = (
    path('<int:pk>/', views.show_profile, name="show profile"),
    path('change_profile_picture/<int:pk>/', views.change_profile_photo, name="change profile photo"),
)