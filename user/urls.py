from django.contrib import admin
from django.urls import path, include
from . import views

# user/
urlpatterns = [
    path('', views.UserAPI.as_view()),
    path('login/', views.UserLoginAPI.as_view()),
]
