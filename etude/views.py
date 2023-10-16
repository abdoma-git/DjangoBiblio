from django.shortcuts import render

def afficher_index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def dossier(request):
    return render(request, 'dossier.html')


