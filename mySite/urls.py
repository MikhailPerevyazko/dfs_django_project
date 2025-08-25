from django.urls import path
from . import views


urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
]
