from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('about/', views.about, name='about'),
    path('help/', views.help_page, name='help_page'),
]
