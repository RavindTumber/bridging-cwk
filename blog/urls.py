from django.urls import path
from . import views

# URL configuration for our blog web app

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
