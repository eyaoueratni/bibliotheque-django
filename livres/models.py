
from django.db import models
from datetime import date

class Livre(models.Model):
    titre = models.CharField(max_length=200)  
    auteur = models.CharField(max_length=100) 
    date_publication = models.DateField()  
    disponible = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.titre} by {self.auteur}"

class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)  
    nom_emprunteur = models.CharField(max_length=100)  
    date_emprunt = models.DateField(default=date.today)  

    def __str__(self):
        return f"{self.nom_emprunteur} borrowed {self.livre.titre}"

class Album(models.Model):
    myimage=models.ImageField(upload_to="images")
   