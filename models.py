from django.db import models
from django.conf import settings
import django.db

class ArticleIdentifiant(models.Model):
    identifiant = models.IntegerField()
"""
class elvis(models.Model):
    a = models.IntegerField()
"""
class ArticleLocationIdentifiant(models.Model):
    identifiant = models.IntegerField()
    
class ForumIdentifiant(models.Model):
    identifiant = models.IntegerField()

class VendeurIdentifiant(models.Model):
    identifiant = models.IntegerField()

class ArticleCategorieSave(models.Model):
    date_frist_creation = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution")
    date_last_modification = models.DateTimeField(auto_now=True, verbose_name="Date de la dernière modification")
    
    nom = models.CharField(max_length = 30)
    photo = models.ImageField(upload_to = settings.MEDIA_ROOT+ "imgs/categorie/")

class VendeurEnregistrer(models.Model):

    date_frist_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de parution")
    date_last_modification = models.DateTimeField(auto_now=True, verbose_name="Date de la dernière modification")
 
    nom = models.CharField(max_length = 100)
    
    prenom = models.CharField(max_length = 100)

    pseudo = models.CharField(max_length = 30)
    
    sexe = models.CharField(max_length = 10)
    
    identifiant = models.IntegerField()
    
    mot_de_passe = models.CharField(max_length = 20)

    code_postal = models.CharField(max_length = 20)

    numero = models.CharField(max_length = 30)

    email = models.EmailField()

    photo_de_profil = models.ImageField(upload_to = settings.MEDIA_ROOT+ "imgs/vendeur/profils/",default = "")

    photo_carte_identite = models.ImageField(upload_to = settings.MEDIA_ROOT+ "imgs/vendeur/")

    photo_de_facture = models.ImageField(upload_to = settings.MEDIA_ROOT+ "imgs/vendeur/")
    
    parrain_1 = models.ForeignKey('VendeurEnregistrer', default=1, verbose_name="VendeurEnregistrer", on_delete=models.SET_DEFAULT)
    parrain_2 = models.ForeignKey('AcheteurEnregistrer', default=1, verbose_name="AcheteurEnregistrer", on_delete=models.SET_DEFAULT)
    
    
class AcheteurEnregistrer(models.Model):
    identifiant = models.IntegerField(default = 2)
    
    date_frist_creation = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution")
    
    date_last_modification = models.DateTimeField(auto_now=True, verbose_name="Date de la dernière modification")
    
    nom = models.CharField(max_length = 100)
    
    prenom = models.CharField(max_length = 100)

    pseudo = models.CharField(max_length = 30)
    
    sexe = models.CharField(max_length = 10)
    
    mot_de_passe = models.CharField(max_length = 20)
    
    numero = models.CharField(max_length = 30)

    email = models.EmailField()

    photo_de_profil = models.ImageField(upload_to = settings.MEDIA_ROOT+ "imgs/acheteur/profils/",default = "")
    
    parrain_1 = models.ForeignKey('VendeurEnregistrer', default=1, verbose_name="VendeurEnregistrer", on_delete=models.SET_DEFAULT)
    parrain_2 = models.ForeignKey('AcheteurEnregistrer', default=1, verbose_name="AcheteurEnregistrer", on_delete=models.SET_DEFAULT)
  
  
class ArticleEnregistrer(models.Model):
    
    identifiant = models.IntegerField(default = 1)
    date_frist_creation = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution")
    date_last_modification = models.DateTimeField(auto_now=True, verbose_name="Date de la dernière modification")
    # Nom
    nom = models.CharField(max_length = 50)
    prix_en_franc_CFA = models.FloatField()
    commentaire = models.CharField(max_length = 100)
    
    vendeur = models.ForeignKey('VendeurEnregistrer', default=1, verbose_name="VendeurEnregistrer", on_delete=models.SET_DEFAULT)
    categorie = models.ForeignKey('ArticleCategorieSave', default=1, verbose_name="ArticleCategorieSave", on_delete=models.SET_DEFAULT)
    
    
    point_tendance = models.IntegerField(default = 0)
    
    date_mise_en_ligne = models.DateTimeField(auto_now_add = True,
                                              auto_now = False,
                                              verbose_name="Date de parution")
    
    nb_de_vente = models.IntegerField(default = 0)
    
    nb_de_vente_depuis_24h = models.IntegerField(default = 0)
    
    nombre_en_stock = models.IntegerField(default = 0)
    
    nombre_de_vente_maximal_par_achat = models.IntegerField(default = 0)

    reduction_de_prix = models.FloatField(default = 0)
    dossier_vendeur = ""
    photo_1 = models.ImageField(upload_to = "second/article/")
    photo_2 = models.ImageField(upload_to = "second/article/")
    photo_3 = models.ImageField(upload_to = "second/article/")

    def __nom__(self):
        return self.nom
    def __point_tendance__(self):
        return self.point_tendance
    def __commentaire__(self):
        return self.commentaire
    def __nb_de_vente__(self):
        return self.nb_de_vente
    def __nb_de_vente_depuis_24h__(self):
        return self.nb_de_vente_depuis_24h
    def __nombre_en_stock__(self):
        return self.nombre_en_stock
    def __nombre_de_vente_maximal_par_achat__(self):
        return self.nombre_de_vente_maximal_par_achat
    def __reduction_de_prix__(self):
        return self.reduction_de_prix


class Forum(models.Model):
    identifiant = models.IntegerField()
    nom = models.CharField(max_length = 60)

    question = models.CharField(max_length = 60)
    
    date_frist_creation = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution")
    date_last_modification = models.DateTimeField(auto_now=True, verbose_name="Date de la dernière modification")
    
    photo = models.ImageField(upload_to = settings.MEDIA_ROOT+ "imgs/forums/")

    contenu = models.CharField(max_length = 10**6)
    poseur_de_question = models.ForeignKey('VendeurEnregistrer', default=1, verbose_name="VendeurEnregistrer", on_delete=models.SET_DEFAULT)

    a = []
    
class LocationArticleSave(models.Model):
    titre = models.CharField(max_length = 60)
    commentaire = models.CharField(max_length = 100)
    
    photo_1 = models.ImageField(upload_to = "second/immobilier/location/")
    photo_2 = models.ImageField(upload_to = "second/immobilier/location/")
    photo_3 = models.ImageField(upload_to = "second/immobilier/location/")
    
    date_frist_creation = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution")
    date_last_modification = models.DateTimeField(auto_now=True, verbose_name="Date de la dernière modification")

    vendeur = models.ForeignKey('VendeurEnregistrer', default=1, verbose_name="VendeurEnregistrer", on_delete=models.SET_DEFAULT)
    identifiant = models.IntegerField(default = 0)
    
    

