from django.urls import path
from . import views

# URL configuration for our CV web app

urlpatterns = [
    path('', views.display_cv, name='display_cv'),
]
