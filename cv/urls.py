from django.urls import path
from . import views

# URL configuration for our CV web app

app_name = 'cv'
urlpatterns = [
    path('', views.display_cv, name='display_cv'),
    path('education/new/', views.education_new, name='education_new'),
    path('education/<int:pk>/edit/', views.education_edit, name='education_edit'),
    path('education/<int:pk>/remove/', views.education_remove, name='education_remove'),
]
