from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path("abdou/", views.afficher_index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dossier/", views.dossier, name="dossier"),

]