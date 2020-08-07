from django.urls import path
from . import views

# URL configuration for our CV web app

app_name = 'cv'
urlpatterns = [
    path('', views.display_cv, name='display_cv'),

    path('education/new/', views.education_new, name='education_new'),
    path('education/<int:pk>/edit/', views.education_edit, name='education_edit'),
    path('education/<int:pk>/remove/', views.education_remove, name='education_remove'),

    path('volunteering/new/', views.volunteering_new, name='volunteering_new'),
    path('volunteering/<int:pk>/edit/', views.volunteering_edit, name='volunteering_edit'),
    path('volunteering/<int:pk>/remove/', views.volunteering_remove, name='volunteering_remove'),

    path('employment/new/', views.employment_new, name='employment_new'),
    path('employment/<int:pk>/edit/', views.employment_edit, name='employment_edit'),
    path('employment/<int:pk>/remove/', views.employment_remove, name='employment_remove'),
]
