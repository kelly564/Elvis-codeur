LINKS= {}


# Pour les acheteur 
LINKS["acc-vent"] = ('acceuil/vente',)
LINKS["acc-loca"] = ("acceuil/location",)
LINKS["acc-louer"] = ("acceuil/louer/<int:ident>","acceuil/louer/",)
LINKS["acc-ache"] = ("acceuil/acheter/<int:identifiant>",
                        "acceuil/acheter/")
LINKS["acc-cate"] = ("acceuil/catégorie",)
LINKS["acc-ven-cate"] = ("acceuil/vente/categorie/<str:categorie>",
                         "acceuil/vente/categorie/",)
                         
LINKS["ach-ins"] = ("acheteur/inscription",)
LINKS["ach-vue-gene"] = ("acheteur/vue_generale/<int:acheteur_identifiant>",
                         "acheteur/vue_generale/",)
LINKS["ach-achat"] = ("acceuil/acheteur/acheter/<int:acheteur_identifiant>",
                       "acceuil/acheteur/acheter/")
                       


# Pour les vendeur

LINKS["vend-ins"] = ('vendeur/inscription',)
LINKS["vend-vue-gene"] = ("vendeur/vue_generale/<int:vendeur_identifiant>",
                          "vendeur/vue_generale/",)
LINKS["vend-conn"] = ('vendeur-connection',)
LINKS["vend-art-ajout"] = ("vendeur/article-ajout/<int:vendeur_identifiant>",
                           "vendeur/article-ajout/",)
LINKS["vend-voir-art"] = ('vendeur/voir-ses-articles/<int:vendeur_identifiant>',
                          'vendeur/voir-ses-articles/',)
LINKS["vend-mod-info"] = ("vendeur/modifier-info/<int:vendeur_identifiant>",
                          "vendeur/modifier-info/",)
LINKS["vend-mod-art"] = ('vendeur/modifier-article/<int:vendeur_identifiant>/<int:article_identifiant>',
                     'vendeur/modifier-article/',)
LINKS["vend-mod-loc-art"] = ("vendeur/modifier-article-location/<int:vendeur_identifiant>/<int:article_identifiant>",
                             "vendeur/modifier-article-location/",)
LINKS["vend-suppr-art"] = ("vendeur/supprimer/<int:article_identifiant>",
                           "vendeur/supprimer/",)
LINKS["vend-loc-art-ajout"] = ("vendeur/ajouter-une-annonce-de-location/<int:vendeur_identifiant>",
                               "vendeur/ajouter-une-annonce-de-location/",)
LINKS["vend-suppr-loc-art"] = ('vendeur/supprimer-location/<int:article_identifiant>',
                               "vendeur/supprimer-location/",)
LINKS["vend-voir-loc-art"] = ("vendeur/voir-ses-annonces-de-location/<int:vendeur_identifiant>",
                              "vendeur/voir-ses-annonces-de-location/",)
