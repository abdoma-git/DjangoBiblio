from django.shortcuts import render, redirect

from etude.models import Etudiant


def afficher_index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def registration(request):
    message = ""
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email= request.POST["email"]
        pwd = request.POST["password"]

        etudiant = Etudiant(first_name=first_name, last_name=last_name, email=email, pwd=pwd)
        if etudiant:
            message = "Etudiant ajouté avec succès"
            etudiant.save()

        else:
            message =" veuillez ressayer "

    return render(request, 'Register.html', context={"abdou":message})


def login(request):

    global utilisateurs
    message = ""
    d = 0
    if request.method == "POST":

        mail = request.POST["email"]
        password = request.POST["password"]

        utilisateurs = Etudiant.objects.raw("SELECT * FROM etude_Etudiant")

        for utilisateur in  utilisateurs:

            if (utilisateur.email == mail and utilisateur.pwd == password):

                request.session['fname'] = utilisateur.first_name
                request.session['lname'] = utilisateur.last_name
                request.session['mail'] = utilisateur.email

                d = 1

                if d == 1:

                    return redirect('dashboard')
                else:
                    message = "Ce compte n'existe pas !!!"


    return render(request, 'login.html', context={"message":message})

def logout(request):
    request.session['fname'] = None
    request.session['lname'] = None
    request.session['mail'] = None
    return redirect('login')


def page(request):
    return render(request, 'page.html')

def creer_livres(request):
    return render(request, 'creer_livres.html')





