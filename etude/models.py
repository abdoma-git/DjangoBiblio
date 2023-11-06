from django.db import models

class Etudiant(models.Model):
   id = models.AutoField(primary_key=True)
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=20)
   email = models.EmailField()
   pwd = models.CharField(max_length=15)




class Livres(models.Model):
   id = models.AutoField(primary_key=True)
   titre = models.CharField(max_length=20)
   categorie = models.CharField(max_length=20)
   nombre_page = models.IntegerField()
   auteur = models.CharField(max_length=15)