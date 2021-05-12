from second.models import *
from second.models import *

###########################
def get_vendeur_by_ID(ident):
    z = VendeurEnregistrer.objects.all()
    for i in z:
        if ident == i.identifiant:
            return i
        
def create_parreine_view(object_):
    
    a = generate_div(_class = "div1",
                 text =  generate_img(width = 257,height = 257,src =object_.photo_de_profil.path,
                                     figcap = object_.nom,figcap_class = "text",alt = "",
                                     figcap_type = "link",figcap_href = ""))
    return a

   
###########################

def create_parrainé_view(a):
    dic = {}
    dic["nom"] = a.nom
    
def generer_forum_message(a):
    dic = {}
    dic["nom"] = a.nom
    dic["message"] = a.message
    
def generer_forum_overview():
    a = ""
    for i in Forum.objects.all():
        a = a + 1
   
def create_article_view(a):
    dic = {}
    dic['nom'] = a.nom
    dic["commentaire"] = a.commentaire
    dic["action"] = "acheter/"+str(a.identifiant)
    dic["img_src"] = a.photo_1.path
    dic["prix"] =  a.prix_en_franc_CFA
    dic["identifiant"] = a.identifiant
    return generate_article(dic)

def create_vendeur_article_view(a,vendeur_identifiant,article_identifiant):
    dic = {}
    dic["vend-ident"] = article_identifiant
    dic['nom'] = a.nom
    dic["commentaire"] = a.commentaire
    dic["action"] = '/second/vendeur/modifier-article/'+str(vendeur_identifiant)+ "/"+str(article_identifiant)
    dic["img_src"] = a.photo_1.path
    dic["prix"] =  a.prix_en_franc_CFA
    dic["identifiant"] = a.identifiant
    return generate_article(dic,True)


def create_categorie_view(i):
    dic = {}
    dic["img_src"] = i.photo.path
    dic["nom"] = i.nom
    dic["action"] = "/second/acceuil/vente/categorie/"+i.nom
    
    a = generate_div(_class = "div1",
                 text =  generate_img(width = 257,height = 257,src = dic["img_src"],
                                     figcap = dic["nom"],figcap_class = "text",alt = "Photo de "+str(dic["nom"]),
                                     figcap_type = "link",figcap_href = dic["action"]))
    return a
    
def generate_article(dic,button = False,code =""" <div>
                            <form>
                            <button class = "delete-button" 
                            type="submit" formaction= "/second/vendeur/supprimer/"""):
    
    if button:
        a = generate_div(_class = "div1",
                 text = code + str(dic["vend-ident"])+ """ ">Supprimer</button>
                            </form>
                        </div> """+  generate_img(width = 257,height = 257,src = dic["img_src"],
                                     figcap = dic["nom"],figcap_class = "text",alt = "Photo de "+str(dic["nom"]),
                                     figcap_type = "link",figcap_href = dic["action"]))
                         
                    
        return a
    else:
        a = generate_div(_class = "div1",
                 text =  generate_img(width = 257,height = 257,src = dic["img_src"],
                                     figcap = dic["nom"],figcap_class = "text",alt = "Photo de "+str(dic["nom"]),
                                     figcap_type = "link",figcap_href = dic["action"]))

        return a
    
                       
                          

def generate_img(width= "",height = "",_class =  "",src = "",
                 figcap = "",figcap_class = "",alt = "",
                 figcap_type = "",figcap_href = "",static = True):
    if(static):
        
        """ width,heigth,_class,src,

        figcap,figcap_class,alt,
                 
        figcap_type,figcap_href """
        text = """ """
        if(width):
            width = ' width = "'+str(width)+ '"'
        else:
            width = ""
        
        if(height):
            height = ' height = "'+str(height)+'"'
        else:
            height = ""

        if(_class):
            _class = ' class = "'+_class+ '"'
        else:
            _class = ""

        if(figcap_class):
            figcap_class = ' class = "'+str(figcap_class)+'"'

        if(alt):
            alt = ' alt = "'+str(alt)+'"'

        if(figcap):
            if(figcap_type == "link"):
                figcap = '<figcaption> <a href = "'+str(figcap_href)+ '"'+\
                     figcap_class+'>'+str(figcap)+'</a> </figcaption>'

        text = text+""" <img src = "{% static '"""+str(src)+"""' %}" """
        text = text + alt+width+height+"/> \n"
        text = text + str(figcap) 
        return text
    else:
        """ width,heigth,_class,src,

        figcap,figcap_class,alt,
                 
        figcap_type,figcap_href """
        text = """ """
        if(width):
            width = ' width = "'+str(width)+ '"'
        else:
            width = ""
        
        if(height):
            height = ' height = "'+str(height)+'"'
        else:
            height = ""

        if(_class):
            _class = ' class = "'+_class+ '"'
        else:
            _class = ""

        if(figcap_class):
            figcap_class = ' class = "'+str(figcap_class)+'"'

        if(alt):
            alt = ' alt = "'+str(alt)+'"'

        if(figcap):
            if(figcap_type == "link"):
                figcap = '<figcaption> <a href = "'+str(figcap_href)+ '"'+\
                     figcap_class+'>'+str(figcap)+'</a> </figcaption>'

        text = text+""" <img src = " """+str(src)+""" " """
        text = text + alt+width+height+"/> \n"
        text = text + str(figcap)
        return text
        

def generate_p(_class ="",text=""):
    """ _class, text"""
    if(_class):
        if(text):
            return '<p '+ ' class = "'+str(_class)+ '"> \n \t' +str(text)+' \n</p>'
        else:
            return '<p '+ ' class = "'+str(_class)+ '"> \n </p>'
    else:
        if(text):
            return '<p> \n \t ' +str(text)+'\n</p>'
        else:
            return '<p>\n \t </p>'
def generate_div(_class ="",text =""):
    """ _class, text"""
    if(_class):
        if(text):
            return '<div '+ ' class = "'+str(_class)+ '"> \n \t' +str(text)+' \n</div>'
        else:
            return '<div '+ ' class = "'+str(_class)+ '"> \n </div>'
    else:
        if(text):
            return '<div> \n \t ' +str(text)+'\n</div>'
        else:
            return '<div>\n \t </div>'
        
def generate_figure(_class ="", text =""):
    """ _class, text"""
    if(_class):
        if(text):
            return '<figure '+ ' class = "'+str(_class)+ '"> \n \t' +str(text)+' \n</figure>\n'
        else:
            return '<figure '+ ' class = "'+str(_class)+ '"> \n </figure>\n'
    else:
        if(text):
            return '<figure> \n \t ' +str(text)+'\n</figure>\n'
        else:
            return '<figure>\n \t </figure>\n'

def generate_title(title):
    """ title """
    if(title):
        return '<title>{% block title %} '+ str(title)+ '{% endblock %}</title>'

    else:
        return '<title>{% block title %}  {% endblock %}</title>\n'
def generate_meta(charset):
    """ charset """
    return '<meta charset = "'+str(charset)+ '" />\n'

    

def generate_link(rel,_type,href):
    """ rel,_type,href """
    return """<link rel = " """+str(rel)+""" " type = " """+str(_type)+ \
           """ " href = "{% static '"""+str(href)+ """' %}" />"""

def generate_body(text):
    return "<body> \n \t" +str(text)+ "\n \t</body> \n"
def generate_head(text):
    return "<head> \n \t" +str(text)+ "\n \t</head> \n"

def generate_html(text,lang):
    return '<!DOCTYPE html> \n\t <html lang = "'+str(lang)+'">'+str(text)+ '/html>\n\t'
    

""" 
print(generate_img(width = 257,height = 257,src = "first/images/1.jpg",
             alt = "Photo de T-shirt",
             ))

a =  generate_img(width = 257,height = 257,src = "first/images/1.jpg",
             figcap = "T-shirt",figcap_class = "text",alt = "Photo de T-shirt",
             figcap_type = "link")

print(generate_div(_class = "div1",
                   text = a))

print(generate_link(rel = "stylesheet",
                    _type = "text/css",
                    href = "first/vente_style.css"))

print(generate_meta("UTF-8"))
print(generate_title("Page de vente des T-shirt"))

"""
#print(generate_article({
#    "nom":"T-shirt",
#    "action": "/second/vente",
#    "img_src": "first/images/1.jpg",
#    "commentaire": """Si le formulaire est valide, un nouvel attribut de l’objet form est apparu, il nous permettra
#d’accéder aux données : cleaned_data. Ce dernier va renvoyer un dictionnaire contenant
#comme clés les noms de vos différents champs (les mêmes noms qui ont été renseignés dans la
#déclaration de la classe), et comme valeurs les données validées de chaque champ. Par exemple,
#nous pourrions accéder au sujet du message ainsi :""",
#    "prix":"2000"}))


def generate_vendeur_general_view(dic):
    a = """
            {% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel="stylesheet" type = "text/css" href="{% static 'second/vendeur_view_style.css' %}">
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
                        
                    </ul>
                </div>
            </nav>
            """
    b = AcheteurEnregistrer.objects.filter(parrain_1 = get_vendeur_by_ID(dic["vend-ident"]))
    x = VendeurEnregistrer.objects.filter(parrain_1 = get_vendeur_by_ID(dic["vend-ident"]))
    for i in b:
        a = a + "\n" + create_parreine_view(i)
    for i in x:
        a = a + "\n" + create_parreine_view(i) 
        
    a = a + """</body>
        
    </html>"""
            
    

        
    return a


def generate_forum_m(dic):
    a = """
            <div class = "m-div">
            <div>
                <span class = "p-name">"""+dic['nom']+"""</span>
            </div>
            <pre class = "m-pre">"""+\
                dic["message"]+"""
            </pre>
            
        </div>
        """
    return a

def generate_achat_full(dic):
    a = """ {% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel="stylesheet" type = "text/css" href="{% static 'second/acheter_style.css' %}">
            <title>{% block title %}formulaire d'incription du projet ahomenou{% endblock %}</title>
        </head>
        <body>

            <section>
                <article class =  "p-art">
                    <div class = "div1">"""+ generate_img(width = "100%",height = "600px",src = dic["img"],
             alt = "Photo de T-shirt"
             )+ """</div>
                </article>
                <aside class = "a-part">
                    <p class = "prix">Prix : """+str(dic["prix"])+ """ franc CFA </p>
                    <div class = "butt">
                        <button type="button" onclick="alert('Hello world!')" submit = " """ +dic["buy-link"]+ """ ">Acheter</button>
                    </div>
                    <div class = "comm"> """+ dic["commentaire"]+ """ /div>
                </aside>
                
                   
            </section>
            
        </body>

    </html>"""
    return a




def generate_location_full(dic):
    a = """{% load static %}
<!DOCTYPE html>
    <html lang = "fr">
        <head>
            <meta charset = "UTF-8"/>
            <link rel="stylesheet" type = "text/css" href="{% static 'second/location_deep_style.css' %}">
            <title>{% block title %}formulaire d'incription du projet ahomenou{% endblock %}</title>
        </head>
        <body>

            <section>
                <article class =  "p-art">
                    <div class = "div1">
                    """+generate_img(width = 150,height = 150,src = dic["vend-img"],
             alt = "Photo de T-shirt"
             )+"""

                    <p>"""+str(dic["loc-comm"])+""" </p> 
                    </div>
                </article>

                <aside class = "photo1">
                    <figure>
                        <div class = "div1">
                        """ + generate_img(width = "100%",height = "90%",src = dic["img-1"],
             alt = "Photo de T-shirt"
             )+""" 
                            
                        </div>
                    </figure>
                </aside>

                <article class = "photo2">
                    <figure>
                        <div class = "div1">
                        """+ generate_img(width = "100%",height = "100%",src = dic["img-1"],
             alt = "Photo de T-shirt"
             )+""" 
                            
                        </div>
                    </figure>
                </article>

                <article class ="photo3">
                    <figure>
                        <div class = "div1">
                        """ + generate_img(width = "100%",height = "100%",src = dic["img-1"],
             alt = "Photo de T-shirt"
             )+ """
                            
                        </div>
                    </figure>
                </article>
    
            <article>
                <p class = "contact" >Contacter <a href = " """+dic["contact-link"]+\
                """ "> l'annoceur </a></p>
            </article>
            </section>
            
        </body>

    </html> """

    return a











    
