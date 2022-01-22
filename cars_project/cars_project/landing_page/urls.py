from django.urls import path
from cars_project.landing_page import views


urlpatterns = (
    path('', views.index, name='landing page'),
)