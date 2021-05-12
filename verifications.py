from django.views.generic import *

import os
import time
import random
from second.forms import VendeurConnect,Article,Vendeur,Image
from second.models import *
from second.generer_html import generate_article
# Create your views here.


def generate_article_id():
    if len(ArticleIdentifiant.objects.all()) != 0:
        
        result = False
        a = 0
        while not result:
            a = random.randint(2**7,10**13)
            r = []
            for i in ArticleIdentifiant.objects.all():
                r.append(i.identifiant)
            if a in r:
                result = False
            else:
                result = True
        return a
    else:
        return random.randint(2**7,10**13)
    
def generate_forum_id():
    if len(Forum.objects.all()) != 0:
        
        result = False
        a = 0
        while not result:
            a = random.randint(2**7,10**13)
            r = []
            for i in Forum.objects.all():
                r.append(i.identifiant)
            if a in r:
                result = False
            else:
                result = True
        return a
    else:
        return random.randint(2**7,10**13)
    
def generate_location_article_id():
    if len(LocationArticleSave.objects.all()) != 0:
        
        result = False
        a = 0
        while not result:
            a = random.randint(2**7,10**13)
            r = []
            for i in LocationArticleSave.objects.all():
                r.append(i.identifiant)
            if a in r:
                result = False
            else:
                result = True
        return a
    else:
        return random.randint(2**7,10**13)
    
def is_vendeur_exist(ident):
    z = VendeurEnregistrer.objects.all()
    T = False
    for i in z:
        if ident == i.identifiant:
            T = True
            return T
    return T

def is_article_exist(ident):
    z = ArticleEnregistrer.objects.all()
    T = False
    for i in z:
        if ident == i.identifiant:
            T = True
            return T
    return T

def is_location_article_exist(ident):
    z = LocationArticleSave.objects.all()
    T = False
    for i in z:
        if ident == i.identifiant:
            T = True
            return T
    return T
def get_categorie_by_Name(nom):
    z = ArticleCategorieSave.objects.all()
    for i in z:
        if nom == i.nom:
            return i
        
def get_vendeur_by_ID(ident):
    z = VendeurEnregistrer.objects.all()
    for i in z:
        if ident == i.identifiant:
            return i
        
def get_acheteur_by_ID(ident):
    z = AcheteurEnregistrer.objects.all()
    for i in z:
        if ident == i.identifiant:
            return i       
def get_article_by_ID(ident):
    z = ArticleEnregistrer.objects.all()
    for i in z:
        if ident == i.identifiant:
            return i

def get_location_article_by_ID(ident):
    z = LocationArticleSave.objects.all()
    for i in z:
        if ident == i.identifiant:
            return i
        
def verificate_vendeur_save(dic):
    z = VendeurEnregistrer.objects.all()
    a = True
    if(len(z) >0):
        for i in z:
            if dic['identifiant'] == i.identifiant:
                a = False
                return a
        return a
    else:
        return True
              
def verificate_acheteur_save(dic):
    z = AcheteurEnregistrer.objects.all()
    a = True
    if(len(z) >0):
        for i in z:
            if dic['identifiant'] == i.identifiant:
                a = False
                return a
        return a
    else:
        return True   
                

def save_categorie(dic):
    a = ArticleCategorieSave()
    a.nom = dic["nom"]
    a.photo = dic["photo"]
    a.save()

def save_article(dic):
    #L'article
    a = ArticleEnregistrer()

    c = get_categorie_by_Name(dic["categorie"][0])

    #print("\n\n\n",c,"\n\n\n\n")
    # Le vendeur
    v = dic["vend-ident"]
    #
    a.nom = dic['nom']
    a.vendeur = v
    a.prix_en_franc_CFA = dic['prix_en_franc_CFA']
    a.commentaire = dic['commentaire']
    a.photo_1 = dic['photo_1']
    a.photo_2 = dic['photo_2']
    a.photo_3 = dic['photo_3']
    r = generate_article_id()
    a.identifiant = r
    id_ = ArticleIdentifiant()
    id_.identifiant = r
    a.categorie = c
    id_.save()
    a.save()
    #print(create_article_view(a))

def modify_article(a,dic):
    c = get_categorie_by_Name(dic["categorie"][0])

    #print("\n\n\n",c,"\n\n\n\n")
    # Le vendeur
    v = dic["vend-ident"]
    #
    a.nom = dic['nom']
    a.vendeur = v
    a.prix_en_franc_CFA = dic['prix_en_franc_CFA']
    a.commentaire = dic['commentaire']
    a.photo_1 = dic['photo_1']
    a.photo_2 = dic['photo_2']
    a.photo_3 = dic['photo_3']
    r = generate_article_id()
    a.identifiant = r
    id_ = ArticleIdentifiant()
    id_.identifiant = r
    a.categorie = c
    id_.save()
    a.save()
   
def save_acheteur(dic):
    a = AcheteurEnregistrer()
    a.nom = dic["nom"]
    a.prenom = dic["prenom"]
    a.pseudo  = dic["pseudo"]
    a.sexe = dic["sexe"][0]
    a.identifiant = dic['identifiant']
    a.mot_de_passe  = dic['mot_de_passe']
    a.numero = dic['numero']
    a.email = dic['email']
    a.photo_de_profil = dic['photo_de_profil']
    a.save()
def save_vendeur(dic):
    a = VendeurEnregistrer()
    a.nom = dic["nom"]
    a.prenom = dic["prenom"]
    a.pseudo  = dic["pseudo"]
    a.sexe = dic["sexe"][0]
    a.identifiant = dic['identifiant']
    a.mot_de_passe  = dic['mot_de_passe']
    a.code_postal = dic['code_postal']
    a.numero = dic['numero']
    a.email = dic['email']
    a.photo_de_profil = dic['photo_de_profil']
    a.photo_carte_identite = dic['photo_carte_identite']
    a.photo_de_facture = dic['photo_de_facture']
    a.save()

def modify_vendeur(a,dic):
    
    a.nom = dic["nom"]
    a.prenom = dic["prenom"]
    a.pseudo  = dic["pseudo"]
    a.sexe = dic["sexe"][0]
    a.identifiant = dic['identifiant']
    a.mot_de_passe  = dic['mot_de_passe']
    a.code_postal = dic['code_postal']
    a.numero = dic['numero']
    a.email = dic['email']
    a.photo_de_profil = dic['photo_de_profil']
    a.photo_carte_identite = dic['photo_carte_identite']
    a.photo_de_facture = dic['photo_de_facture']
    a.save()


def save_forum(dic):
    f = Forum()
    f.identifiant = generate_forum_id()
    f.nom = dic["nom"]
    f.question = dic["question"]
    f.photo = dic["photo"]
    f.contenu = dic["cont"]
    f.poseur_de_question = dic["vend-ident"]
    f.save()
    
def save_location_article(dic):
    f = LocationArticleSave()
    f.titre  = dic['titre']
    f.commentaire = dic['commentaire']
    a = generate_location_article_id()

    print("\n\n\n\n",a,"\n\n\n\n")
    
    f.identiant = a
    f.vendeur = dic["vend-ident"]
    f.photo_1 = dic["photo_1"]
    f.photo_2 = dic["photo_2"]
    f.photo_3 = dic["photo_3"]
    f.save()

def modify_location_article(f,dic):
    f.titre  = dic['titre']
    f.commentaire = dic['commentaire']
    f.vendeur = dic["vend-ident"]
    f.photo_1 = dic["photo_1"]
    f.photo_2 = dic["photo_2"]
    f.photo_3 = dic["photo_3"]
    f.save()


a = """ sjunvslkjsfd nqljdbs qlsdd  lsqj
&&&&&&&& dpojmdsjds qldsjblkqs  qsldbhjlss bqsh  dsjlqh &&&&&&&&
lhqnlk  ldsqhbdsqj  &&&&&&&& """

def cut_forum_text(text):
    i = 0
    a = []
    u = 0
    while i < len(text):
        if(text[i] == "&" and i+7 < len(text)-1):
            #print(text[i:i+7])
            a.append(text[u+1:i])
            i = i+7
            u = i
        i = i + 1

    return a
