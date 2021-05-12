from django.test import TestCase


from models import VendeurEnregistrer,ArticleEnregistrer,ArticleIdentifiant

a = VendeurEnregistrer.objects.all()
print(a)

# Create your tests here.
