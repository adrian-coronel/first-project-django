# AQUI IRÁN LAS URLS DE ESTA APP
from django.urls import path
from . import views

urlpatterns = [
  path('welcome/', views.welcome),
  path('about/', views.about)
]