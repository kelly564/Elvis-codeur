from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile

class VendeurConnect(forms.Form):
    """ Pour gérer la connection d'un vendeur à son compte """
    
    identifiant = forms.CharField(max_length = 30,
                                  required = True)
    mot_de_passe = forms.CharField(max_length = 30,
                                   widget =forms.PasswordInput,
                                   required = True)
    def send_email(self):
       print(self.cleaned_data)

class ArticleCategorieForm(forms.Form):
    nom = forms.CharField(max_length = 30)
    photo = forms.ImageField()


class ForumForm(forms.Form):
    nom = forms.CharField(max_length=60,initial ="Le nom de votre Forum")
    question = forms.CharField(max_length=60,initial = "La question de votre forum",
                               required = False)
    photo = forms.ImageField(
                        label = "Une photo de couverture pour votre forum",
                        required =  False
                        )
    
    
class Article(forms.Form):
    nom = forms.CharField(max_length=100,initial ="Le nom de votre article")
    prix_en_franc_CFA = forms.FloatField()
    categorie = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=[('Vêtements Homme','Vêtements Homme'),
                 ('Vêtements Femme','Vêtements Femme'),
                 ('Produit de beauté','Produit de beauté'),
                 ('Mécanique','Mécanique'),
                 ('Automobile','Automobile'),
                 ('Electronique','Electronique'),
                 ('Education',"Education"),
                 ('Fruit',"Fruit"),
                 ('Légume',"Légume"),],
        help_text = "Choisissez une seule catégorie",
                 
    )
    commentaire = forms.CharField(widget=forms.Textarea)
    photo_1 = forms.ImageField()
    photo_2 = forms.ImageField()
    photo_3 = forms.ImageField()


    
    def send_email(self):
       print(self.cleaned_data)

class Image(forms.Form):
    name = forms.CharField()
    geeks_field = forms.ImageField()
    

class Acheteur(forms.Form):
    identifiant = forms.IntegerField()
   
    nom = forms.CharField(max_length = 100)
    
    prenom = forms.CharField(max_length = 100)

    pseudo = forms.CharField(max_length = 30)
    
    sexe = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=[('homme','Homme'),
                 ('femme','Femme'),]
    )
    
    mot_de_passe = forms.CharField(max_length = 30, widget =forms.PasswordInput,required = True)
    
    numero = forms.CharField(max_length = 30)

    email = forms.EmailField()

    photo_de_profil = forms.ImageField(required = True)

class Vendeur(forms.Form):
    """ Pour gérer l'inscription d'un vendeur """
    nom = forms.CharField(max_length = 100,required = True)
    
    prenom = forms.CharField(max_length = 100,required = True)
    
    pseudo = forms.CharField(max_length = 30,required = True)

    sexe = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=[('homme','Homme'),
                 ('femme','Femme'),]
    )
    
    identifiant = forms.IntegerField(required = True)
    
    mot_de_passe = forms.CharField(max_length = 30, widget =forms.PasswordInput,required = True)

    code_postal = forms.CharField(max_length = 20,required = True)

    numero = forms.CharField(max_length = 30,required = True)

    email = forms.EmailField()

    photo_de_profil = forms.ImageField(
                            label = "Une photo pour votre profil",
                            required =  False
                            )
  
    photo_carte_identite = forms.ImageField(
                            label = "Une photo de votre carte d'identité",
                            required =  True
                            )
    photo_de_facture = forms.ImageField(help_text = "Donnez une photo de votre"
                                        " facture d'électricité ou d'eau la plus récente",
                                       required =  True)

    def send_email(self):
       print(self.cleaned_data)

class LocationArticleForm(forms.Form):
    titre = forms.CharField(max_length = 60)
    commentaire = forms.CharField(max_length = 100,widget = forms.Textarea)
    
    photo_1 = forms.ImageField(label = "Une première photo de la maison",
                               required = True)
    photo_2 = forms.ImageField(label = "Une deuxième photo de la maison",
                               required = False)
    photo_3 = forms.ImageField(label = "Une troisième photo de la maison",
                               required = False)
    
    
