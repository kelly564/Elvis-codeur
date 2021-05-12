from django.shortcuts import render
from django.template import loader,Template,Context,RequestContext
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views.generic import *

import os
import time
import random
from second.forms import VendeurConnect,Article,Vendeur,Image,ArticleCategorieForm,ForumForm,LocationArticleForm,Acheteur
from second.models import VendeurEnregistrer,ArticleEnregistrer,ArticleIdentifiant,Forum,LocationArticleSave
from second.generer_html import generate_article
from second.verifications import *
from second.generer_html import *
# Create your views here.


def test_button(request):
    context = {}
    template = loader.get_template("second/vendeur_article.html")
    return HttpResponse(template.render(context,request))
    
"""

class VendeurView(FormView): 
    template_name = 'first/formulaire.html'
    form_class = Vendeur
    success_url = '/first/vente'

    def form_valid(self, form):
        form.send_email()
        return super(VendeurView, self).form_valid(form)

"""
 #
#
##
#
##
#
##
#
##
#
##
#
##
#
##
#
#

    
def acheter(request,identifiant):
    a = ""
    b= get_article_by_ID(identifiant)
    dic = {}
    dic["img"] = b.photo_1.path
    dic["prix"] = b.prix_en_franc_CFA
    dic["commentaire"] = b.commentaire
    dic["buy-link"] = "/second/"
    
    a = generate_achat_full(dic)
    
    context = RequestContext(request,{})
    template = Template(a) 
    return HttpResponse(template.render(context))

def test_art(request):
    a = ""
    for i in ArticleEnregistrer.objects.all():
        a = a+ " \n" + create_article_view(i) 
    
    a = """{% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel = "stylesheet" type = "text/css" href = "{% static 'second/test_a_style.css' %}"/>
            <title>{% block title %}Page de vente du projet ahomenou{% endblock %}</title>
            
        </head>
        <body>
            """+a+ " </body>  </html>"
    #print(a)
    context = RequestContext(request,{})
    template = Template(a) #""
    return HttpResponse(template.render(context))
    

def vendeur_article_view(request,vendeur_identifiant):
    if(is_vendeur_exist(vendeur_identifiant)):
        a = ""
        dic = {"vend-ident":vendeur_identifiant,"aide-link": ""}
        b = ArticleEnregistrer.objects.filter(vendeur = get_vendeur_by_ID(vendeur_identifiant))
        for i in b:
            a = a+ " \n" + create_vendeur_article_view(i,vendeur_identifiant,i.identifiant)

        c = """  
            {% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel="stylesheet" type = "text/css" href="{% static 'second/vendeur_article_view.css' %}">
            <title>{% block title %}formulaire d'incription du projet ahomenou{% endblock %}</title>
        </head>
        <body>
            <nav>
                <div class="table">
                    <ul>
                        <li class="menu-voi">
                            <a href="/second/vendeur/voir-ses-articles/"""+str(dic["vend-ident"])+""" "> Voir vos articles</a>
                        </li>
                        <li class="menu-cont">
                            <a href="/second/vendeur/article-ajout/"""+str(dic["vend-ident"])+ """ " >Ajouter un article</a>
                        </li>
                        <li class="menu-voi">
                            <a href="/second/vendeur/voir-ses-annonces-de-location/"""+str(dic["vend-ident"])+""" "> Voir vos annonces de location</a>
                        </li>
                        <li class="menu-cont">
                            <a href="/second/vendeur/ajouter-une-annonce-de-location/"""+str(dic["vend-ident"])+ """ " >Ajouter une annonce de location</a>
                        </li>
                        
                        <li class="menu-voi">
                            <a href="/second/vendeur/modifier-info/"""+str(dic["vend-ident"])+ """ " >Modififier vos information.</a>
                        </li>
                        <li class="menu-voi">
                            <a href="/second/vendeur/forum/ajout/"""+str(dic["vend-ident"])+ """ " >Ajouter une discution</a>
                        </li>
                        <li class="menu-voi">
                            <a href="/second/vendeur/forum/"""+str(dic["vend-ident"])+ """ " >Voir les forums</a>
                        </li>
                    </ul>
                </div>
            </nav>
            
           <section>
            """+ a+ """
            <section/>
            
        </body>
        
    </html>""" 
        context = RequestContext(request,{})
        template = Template(c) #""
        return HttpResponse(template.render(context))
   
  
def inscription_vendeur(request):
    a = 0
    if request.method == "POST":
        form = Vendeur(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            #print("\n\n\n\n",verificate_vendeur_save(form.cleaned_data),"\n\n\n\n")
            if(verificate_vendeur_save(form.cleaned_data)):
                a = form.cleaned_data["identifiant"]
                r =form.cleaned_data
                print(r)
                save_vendeur(r)
                return HttpResponseRedirect('/second/vendeur/vue_generale/'+str(a))
            else:
                form = Vendeur()
                context = {'form':form,
                           'message': """Veillez changer d'identifiant
                                         s'il vous plaît car celui que vous venez d'entrer est déja utilisé"""}
                
                template = loader.get_template("second/formulaire.html")
                return HttpResponse(template.render(context,request))
                
        else:
            form = Vendeur()
            context = {'form':form,
                           'message': """Vous avez mal entré les informations"""}
            template = loader.get_template("second/formulaire.html")
            return HttpResponse(template.render(context,request))
            
            
    else:
        form = Vendeur()
        context = {'form':form}
        template = loader.get_template("second/formulaire.html")
        return HttpResponse(template.render(context,request))
    
def connection_vendeur(request):
    if request.method == "POST":
        f = VendeurConnect(request.POST,request.FILES)
        if f.is_valid():
            print(f.cleaned_data)
            #print(f.cleaned_data["identifiant"],is_vendeur_exist(f.cleaned_data["identifiant"]))
            
            if(is_vendeur_exist(int(f.cleaned_data["identifiant"]))):
                
                if get_vendeur_by_ID(int(f.cleaned_data["identifiant"])).mot_de_passe == f.cleaned_data["mot_de_passe"]:
                    
                    return HttpResponseRedirect('/second/vendeur/vue_generale/'+str(f.cleaned_data["identifiant"]))
                else:
                    context = {}
                    f = VendeurConnect()
                    context = {'form':f}
                    context["ident_message"] = "Votre mot de passe ne correspond pas"
                    template = loader.get_template("second/vendeur_connection.html")
                    return HttpResponse(template.render(context,request))
            else:
                context = {}
                f = VendeurConnect()
                context = {'form':f}
                context["ident_message"] = "Votre identifiant est erroné"
                template = loader.get_template("second/vendeur_connection.html")
                return HttpResponse(template.render(context,request))
                
        else:
            ontext = {}
            f = VendeurConnect()
            context = {'form':f}
            template = loader.get_template("second/vendeur_connection.html")
            return HttpResponse(template.render(context,request))
            
    else:
        context = {}
        f = VendeurConnect()
        context = {'form':f}
        template = loader.get_template("second/vendeur_connection.html")
        return HttpResponse(template.render(context,request))

def vendeur_modification_info(request,vendeur_identifiant):
    if(is_vendeur_exist(vendeur_identifiant)):
        if request.method == "POST":
            form = Vendeur(request.POST,request.FILES)
            if form.is_valid():
                print(form.cleaned_data)
                #print("\n\n\n\n",verificate_vendeur_save(form.cleaned_data),"\n\n\n\n")
                if(verificate_vendeur_save(form.cleaned_data)):
                
                    save_vendeur(form.cleaned_data)
                else:
                    form = Vendeur()
                    context = {'form':form,
                           'message': """Veillez changer d'identifiant
                                         s'il vous plaît car celui que vous venez d'entrer est déja utilisé"""}
                
                    template = loader.get_template("second/formulaire.html")
                    return HttpResponse(template.render(context,request))
                
                return HttpResponseRedirect('/second/vendeur/vue_generale/'+str(vendeur_identifiant))
            else:
                form = Vendeur()
                context = {'form':form}
                template = loader.get_template("second/formulaire.html")
                return HttpResponse(template.render(context,request))
            
        else:
            form = Vendeur()
            context = {'form':form}
            template = loader.get_template("second/formulaire.html")
            return HttpResponse(template.render(context,request))
    else:
        raise Http404

def vendeur_modifier_article(request,vendeur_identifiant,article_identifiant):
    """ Pour modifier un article articles """
    if(is_vendeur_exist(vendeur_identifiant)):
        if request.method == "POST":
            f = Article(request.POST,request.FILES)
            if f.is_valid():
                r = f.cleaned_data
                r["vend-ident"] = get_vendeur_by_ID(vendeur_identifiant)
                print(r)
                modify_article(get_article_by_ID(article_identifiant),r)
            
                return HttpResponseRedirect('/second/vendeur/vue_generale/'+str(vendeur_identifiant))
            else:
                context = {}
                f = Article()
                context = {'form':f}
                template = loader.get_template("second/article_ajout.html")
                return HttpResponse(template.render(context,request))
                
        
        else:
            context = {}
            f = Article()
            context = {'form':f}
            template = loader.get_template("second/article_ajout.html")
            return HttpResponse(template.render(context,request))
    else:
        raise Http404
        
def create_article(request,vendeur_identifiant):
    """ Pour renseigner les nouveaux articles """
    if(is_vendeur_exist(vendeur_identifiant)):
        if request.method == "POST":
            f = Article(request.POST,request.FILES)
            if f.is_valid():
                r = f.cleaned_data
                r["vend-ident"] = get_vendeur_by_ID(vendeur_identifiant)
                print(r)
                save_article(r)
            
                return HttpResponseRedirect('/second/vendeur/vue_generale/'+str(vendeur_identifiant))
            else:
                context = {}
                f = Article()
                context = {'form':f}
                template = loader.get_template("second/article_ajout.html")
                return HttpResponse(template.render(context,request))
                
        
        else:
            context = {}
            f = Article()
            context = {'form':f}
            template = loader.get_template("second/article_ajout.html")
            return HttpResponse(template.render(context,request))
    else:
        raise Http404
        
def delete_article(request,article_identifiant):
    i = 0
    if is_article_exist(article_identifiant):
        a = get_article_by_ID(article_identifiant)
        vendeur = a.vendeur
        i = vendeur.identifiant 
        a.delete()
        return HttpResponseRedirect('/second/vendeur/voir-ses-articles/'+str(i))
    else:
        return Http404

def ajout_forum(request,vendeur_identifiant):
    """ Pour renseigner les nouveaux articles """
    if(is_vendeur_exist(vendeur_identifiant)):
        if request.method == "POST":
            f = ForumForm(request.POST,request.FILES)
            if f.is_valid():
                r = f.cleaned_data
                r["vend-ident"] = get_vendeur_by_ID(vendeur_identifiant)
                r["cont"] = ""
                print(r)
                save_forum(r)
            
                return HttpResponseRedirect('/second/vendeur/vue_generale/'+str(vendeur_identifiant))
            else:
                context = {}
                f = ForumForm()
                context = {'form':f}
                template = loader.get_template("second/forum_ajout.html")
                return HttpResponse(template.render(context,request))
                
        
        else:
            context = {}
            f = ForumForm()
            context = {'form':f}
            template = loader.get_template("second/forum_ajout.html")
            return HttpResponse(template.render(context,request))
    else:
        raise Http404

def voir_les_forums(request,vendeur_identifiant):
    if(is_vendeur_exist(vendeur_identifiant)):
        a = generer_forum_overview()
        context = RequestContext(request,{})
        template = Template(a) #""
        return HttpResponse(template.render(context))
    else:
        return Http404


def categorie_show(request):
    a = ""
    for i in ArticleCategorieSave.objects.all():
        a = a + "\n "+ create_categorie_view(i)
    a = """{% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel = "stylesheet" type = "text/css" href = "{% static 'second/vente_style.css' %}"/>
            <title>{% block title %}Page de vente du projet ahomenou{% endblock %}</title>
            
        </head>
        <body>
            """+a+ " </body>  </html>"
    #print(a)
    context = RequestContext(request,{})
    template = Template(a) #""
    return HttpResponse(template.render(context))

def vente_categorie(request,categorie):
    a = ""
    for i in ArticleEnregistrer.objects.filter(categorie = get_categorie_by_Name(categorie)):
        a = a+ " \n" + create_article_view(i) 
    
    a = """{% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel = "stylesheet" type = "text/css" href = "{% static 'second/vente_style.css' %}"/>
            <title>{% block title %}Page de vente du projet ahomenou{% endblock %}</title>
            
        </head>
        <body>
            """+a+ " </body>  </html>"
    #print(a)
    context = RequestContext(request,{})
    template = Template(a) #""
    return HttpResponse(template.render(context))
    
def vente(request):
    a = ""
    for i in ArticleEnregistrer.objects.all():
        a = a+ " \n" + create_article_view(i) 
    
    a = """{% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel = "stylesheet" type = "text/css" href = "{% static 'second/vente_style.css' %}"/>
            <title>{% block title %}Page de vente du projet ahomenou{% endblock %}</title>
            
        </head>
        <body>
            """+a+ " </body>  </html>"
    #print(a)
    context = RequestContext(request,{})
    template = Template(a) #""
    return HttpResponse(template.render(context))

def vendeur_view(request,vendeur_identifiant):
    dic = {}
    dic["vend-ident"] = vendeur_identifiant
    dic["vend-nb-vente-24"] = 4400
    dic["art-le-plus-avant"] = 203
    dic["aide-link"] = ""
    a = generate_vendeur_general_view(dic)
    context = RequestContext(request,{})
    template = Template(a) #""
    return HttpResponse(template.render(context))


def add_categorie(request):
    if request.method == "POST":
        f = ArticleCategorieForm(request.POST,request.FILES)
        if f.is_valid():
            print(f.cleaned_data)
            save_categorie(f.cleaned_data)
            return HttpResponseRedirect('/second/acceuil/vente')
        else:
            print(f.cleaned_data)
            return HttpResponseRedirect('/second/vendeur/vue_generale')
        
    else:
        context = {}
        f =ArticleCategorieForm()
        context = {'form':f}
        template = loader.get_template("second/add_categorie.html")
        return HttpResponse(template.render(context,request))


#
#
##
#
##
#
##
#
##
#
##
#
##
#
##
#
##
#
#
def location_deep_view(request):
    context = {}
    template = loader.get_template("second/location_deep.html")
    return HttpResponse(template.render(context,request))
    
def vendeur_ajout_location(request,vendeur_identifiant):
    """ Pour renseigner les nouveaux articles """
    if(is_vendeur_exist(vendeur_identifiant)):
        if request.method == "POST":
            f = LocationArticleForm(request.POST,request.FILES)
            if f.is_valid():
                r = f.cleaned_data
                r["vend-ident"] = get_vendeur_by_ID(vendeur_identifiant)
                print(r)
                save_location_article(r)
            
                return HttpResponseRedirect('/second/vendeur/vue_generale/'+str(vendeur_identifiant))
            else:
                context = {}
                f = LocationArticleForm()
                context = {'form':f}
                template = loader.get_template("second/article_ajout.html")
                return HttpResponse(template.render(context,request))
                
        
        else:
            context = {}
            f = LocationArticleForm()
            context = {'form':f}
            template = loader.get_template("second/article_ajout.html")
            return HttpResponse(template.render(context,request))
    else:
        raise Http404


def delete_location_article(request,article_identifiant):
    i = 0
    if is_location_article_exist(article_identifiant):
        a = get_location_article_by_ID(article_identifiant)
        vendeur = a.vendeur
        i = vendeur.identifiant 
        a.delete()
        return HttpResponseRedirect('/second/vendeur/voir-ses-annonces-de-location/'+str(i))
    else:
        return Http404
    
def vendeur_location_article_view(request,vendeur_identifiant):
    if(is_vendeur_exist(vendeur_identifiant)):
        dic = {"vend-ident":vendeur_identifiant}
        a = ""
        b = LocationArticleSave.objects.filter(vendeur = get_vendeur_by_ID(vendeur_identifiant))
        for i in b:
            a = a+ " \n" + create_vendeur_location_article_view(i,vendeur_identifiant,i.identifiant)

        c = """  
            {% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel="stylesheet" type = "text/css" href="{% static 'second/vendeur_article_view.css' %}">
            <title>{% block title %}formulaire d'incription du projet ahomenou{% endblock %}</title>
        </head>
        <body>
            <nav>
                <div class="table">
                    <ul>
                        <li class="menu-voi">
                            <a href="/second/vendeur/voir-ses-articles/"""+str(dic["vend-ident"])+""" "> Voir vos articles</a>
                        </li>
                        <li class="menu-cont">
                            <a href="/second/vendeur/article-ajout/"""+str(dic["vend-ident"])+ """ " >Ajouter un article</a>
                        </li>
                        <li class="menu-voi">
                            <a href="/second/vendeur/voir-ses-annonces-de-location/"""+str(dic["vend-ident"])+""" "> Voir vos annonces de location</a>
                        </li>
                        <li class="menu-cont">
                            <a href="/second/vendeur/ajouter-une-annonce-de-location/"""+str(dic["vend-ident"])+ """ " >Ajouter une annonce de location</a>
                        </li>
                        
                        <li class="menu-voi">
                            <a href="/second/vendeur/modifier-info/"""+str(dic["vend-ident"])+ """ " >Modififier vos information.</a>
                        </li>
                        <li class="menu-voi">
                            <a href="/second/vendeur/forum/ajout/"""+str(dic["vend-ident"])+ """ " >Ajouter une discution</a>
                        </li>
                        <li class="menu-voi">
                            <a href="/second/vendeur/forum/"""+str(dic["vend-ident"])+ """ " >Voir les forums</a>
                        </li>
                    </ul>
                </div>
            </nav>
            
           <section>
            """+a+ "</body>  </html>"
        context = RequestContext(request,{})
        template = Template(c) #""
        return HttpResponse(template.render(context))

def location_view(request):
    a = ""
    b = LocationArticleSave.objects.all()
    print(b)
    for i in b:
        a = a+ " \n" + generate_location_view(i)

    c  = """{% load static %}
        <!DOCTYPE html>
        <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel = "stylesheet" type = "text/css" href = "{% static 'second/vente_style.css' %}"/>
            <title>{% block title %}Page des mainsons en location{% endblock %}</title>
            
        </head>
        <body>
     """+a+ " </body>  </html>"
        
    context = RequestContext(request,{})
    template = Template(c) #""
    return HttpResponse(template.render(context))

def create_vendeur_location_article_view(a,vendeur_identifiant,article_identifiant):
    print(a)
    # Vue pour le vendeur
    dic = {}
    dic['nom'] = a.titre
    dic["vend-ident"] = article_identifiant
    dic["commentaire"] = a.commentaire
    dic["action"] = '/second/vendeur/modifier-article-location/'+str(vendeur_identifiant)+ "/"+str(article_identifiant)
    dic["img_src"] = a.photo_1.path
    dic["identifiant"] = a.identifiant
    return generate_article(dic,True,code = """ <div>
                            <form>
                            <button class = "delete-button" 
                            type="submit" formaction= "/second/vendeur/supprimer-location/""")

def generate_location_view(a):
    # Vue pour l'acheteur
    dic = {}
    dic['nom'] = a.titre
    dic["commentaire"] = a.commentaire
    dic["action"] = '/second/acceuil/louer/'+str(a.identifiant)
    dic["img_src"] = a.photo_1.path
    dic["identifiant"] = a.identifiant
    return generate_article(dic)
    

def vendeur_modifier_location_article(request,vendeur_identifiant,article_identifiant):
    """ Pour modifier un article articles """
    if(is_vendeur_exist(vendeur_identifiant)):
        if request.method == "POST":
            f = LocationArticleForm(request.POST,request.FILES)
            if f.is_valid():
                r = f.cleaned_data
                r["vend-ident"] = get_vendeur_by_ID(vendeur_identifiant)
                r["identifiant"] = article_identifiant
                print(r)
                modify_location_article(get_location_article_by_ID(article_identifiant),r)
            
                return HttpResponseRedirect('/second/vendeur/vue_generale/'+str(vendeur_identifiant))
            else:
                context = {}
                f = LocationArticleForm()
                context = {'form':f}
                template = loader.get_template("second/article_ajout.html")
                return HttpResponse(template.render(context,request))
                
        
        else:
            context = {}
            f = LocationArticleForm()
            context = {'form':f}
            template = loader.get_template("second/article_ajout.html")
            return HttpResponse(template.render(context,request))
    else:
        raise Http404

def location_full_view(request,ident):
    dic = {}
    a = get_location_article_by_ID(ident)
    print(a.identifiant)
    dic["vend-img"] = a.vendeur.photo_carte_identite.path

    
    dic["img-1"] = a.photo_1.path
    dic["img-2"] = a.photo_2.path
    dic["img-3"] = a.photo_3.path
    dic["contact-link"] = "acceuil/location/contact/"+str(ident)
    dic["loc-comm"] = a.commentaire

    text = generate_location_full(dic)
    context = RequestContext(request,{})
    template = Template(text) #""
    return HttpResponse(template.render(context))
    
    
    
    
    
    
    
    
    
    
    
 ######################################################   
def achteur_inscrit_acheter(request,acheteur_identifiant):
    a = ""
    for i in ArticleEnregistrer.objects.all():
        a = a+ " \n" + create_article_view(i) 
    
    a = """{% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel = "stylesheet" type = "text/css" href = "{% static 'second/vente_style.css' %}"/>
            <title>{% block title %}Page de vente du projet ahomenou{% endblock %}</title>
            
        </head>
        <body>
            """+a+ " </body>  </html>"
    #print(a)
    context = RequestContext(request,{})
    template = Template(a) #""
    return HttpResponse(template.render(context))
    
def create_parreine_view(object_):
    
    a = generate_div(_class = "div1",
                 text =  generate_img(width = 257,height = 257,src =object_.photo_de_profil.path,
                                     figcap = object_.nom,figcap_class = "text",alt = "",
                                     figcap_type = "link",figcap_href = ""))
    return a

    

def acheteur_general_view(request,acheteur_identifiant):
    dic = {"vend-ident":acheteur_identifiant}
    a = ""
    b = AcheteurEnregistrer.objects.filter(parrain_2 = get_acheteur_by_ID(acheteur_identifiant))
    x = VendeurEnregistrer.objects.filter(parrain_2 = get_acheteur_by_ID(acheteur_identifiant))
    for i in b:
        a = a+ " \n" + create_parreine_view(i)
        
    for  i in x:
        a = a + "\n "+ create_parreine_view(i)
        
    c = """  
            {% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel="stylesheet" type = "text/css" href="{% static 'second/vendeur_article_view.css' %}">
            <title>{% block title %}formulaire d'incription du projet ahomenou{% endblock %}</title>
        </head>
        <body>
            <nav>
                <div class="table">
                    <ul>
                        <li class="menu-voi">
                            <a href="/second/vendeur/voir-ses-articles/"""+str(dic["vend-ident"])+""" "> Voir votre porte-monnaie</a>
                        </li>
                        <li class="menu-cont">
                            <a href="/second/vendeur/article-ajout/"""+str(dic["vend-ident"])+ """ " >Parainner quelqu'un</a>
                        </li>
                        
                       
                    </ul>
                </div>
            </nav>
            
           <section>
            """+a+ "</body>  </html>"
    context = RequestContext(request,{})
    template = Template(c) #""
    return HttpResponse(template.render(context))
    
def inscription_acheteur(request):
    a = 0
    if request.method == "POST":
        form = Acheteur(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            #print("\n\n\n\n",verificate_vendeur_save(form.cleaned_data),"\n\n\n\n")
            if(verificate_acheteur_save(form.cleaned_data)):
                a = form.cleaned_data["identifiant"]
                r =form.cleaned_data
                print(r)
                save_acheteur(r)
                return HttpResponseRedirect("acheteur/"+str(a))
            else:
                form = Acheteur()
                context = {'form':form,
                           'message': """Veillez changer d'identifiant
                                         s'il vous plaît car celui que vous venez d'entrer est déja utilisé"""}
                
                template = loader.get_template("second/formulaire.html")
                return HttpResponse(template.render(context,request))
                
        else:
            form = Acheteur()
            context = {'form':form,
                           'message': """Vous avez mal entré les informations"""}
            template = loader.get_template("second/formulaire.html")
            return HttpResponse(template.render(context,request))
            
            
    else:
        form = Acheteur()
        context = {'form':form}
        template = loader.get_template("second/formulaire.html")
        return HttpResponse(template.render(context,request))
   
      
 ######################################################
