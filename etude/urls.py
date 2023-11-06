from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.afficher_index, name="index"),
    path("index/", views.afficher_index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("Register/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("page/", views.page, name="page"),
    path("creer_livres/", views.creer_livres, name="newlivre"),

]