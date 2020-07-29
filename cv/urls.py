from django.urls import path
from . import views

# URL configuration for our CV web app

app_name = 'cv'
urlpatterns = [
    path('', views.display_cv, name='display_cv'),
    path('education/new/', views.education_new, name='education_new'),
]
