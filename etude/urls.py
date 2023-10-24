from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.afficher_index, name="index"),
    path("abdou/", views.afficher_index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("Register/", views.registration, name="registration"),
    path("login/", views.login, name="login"),

]