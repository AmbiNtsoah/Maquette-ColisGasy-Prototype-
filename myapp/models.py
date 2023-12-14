from django.db import models

class Utilisateurs(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    MotDePasse = models.CharField(max_length=255)
    TypeUtilisateur = models.CharField(max_length=20, choices=[('conducteur', 'Conducteur'), ('expediteur', 'Expéditeur')])

class Trajets(models.Model):
    LieuDepart = models.CharField(max_length=100)
    LieuArrivee = models.CharField(max_length=100)
    DateHeureDepart = models.DateTimeField()
    DescriptionTrajet = models.TextField()
    EspaceColisDisponible = models.DecimalField(max_digits=10, decimal_places=2)
    PrixTrajet = models.DecimalField(max_digits=10, decimal_places=2)

class Colis(models.Model):
    LieuDepart = models.CharField(max_length=100)
    LieuLivraison = models.CharField(max_length=100)
    DateLivraison = models.DateField()
    DescriptionColis = models.TextField()
    StatutColis = models.BooleanField(default=False)
    conducteur_accepte = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Colis")
        verbose_name_plural = ("Colis")
#Montre le nom d'un objet sur la page admin    
    def ___str__(self):
        return self.name
    
class Correspondances(models.Model):
    StatutCorrespondance = models.CharField(max_length=15, choices=[('en_attente', 'En attente'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée'), ('terminee', 'Terminée'), ('autre', 'Autre')])
