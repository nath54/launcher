#coding:utf-8
#launcher texte
import os,sys
import requests
import zipfile
from os.path import expanduser
home = expanduser("~")

direlauncher="Launcher/"
direjeux="jeux/"
if not direlauncher[:-1] in os.listdir(home):
    os.mkdir(home+"/"+direlauncher)
    os.mkdir(home+"/"+direlauncher+direjeux)

direm=home+"/"+direlauncher
direj=home+"/"+direlauncher+direjeux

def inp(txt):
    vp=sys.version_info
    if vp[0]==2: return raw_input(txt)
    else: return input(txt)

c="#"
cc="|"
ccc=","



def page_jeu_magasin(jeu):
    print("")
    print("#################################################################")
    print("")
    print("Voici la page du jeu "+str(jeu[0]))
    print("")
    print("description : "+str(jeu[2]))
    print("")
    print(" 1-télécharger le jeu")
    print(" q-menu précédent")
    choix=inp(" : ")
    if choix!="q":
        if choix=="1":
            try:
                url=jeu[1]
                req = requests.get(url)
                txxt=""
                for chunk in req.iter_content(1000):
                    txxt+=str(chunk)
                f=open(direj+jeu[0]+".zip","w")
                f.write(txxt)
                f.close()
                zip_ref = zipfile.ZipFile(direj+jeu[0]+".zip","r")
                zip_ref.extractall(direj+jeu[0]+"/")
                zip_ref.close()
                print("Jeu téléchargé.")
            except:
                print("Il y a eu une erreur lors du téléchargement du jeu.")
        page_jeu_magasin(jeu)

def magasin():
    jeux=[]
    try:
        url="https://raw.githubusercontent.com/nath54/launcher_data/master/data.nath"
        req = requests.get(url)
        txxt=""
        for chunk in req.iter_content(1000):
            txxt+=str(chunk)
        f=open(direm+"data.nath","w")
        f.write(txxt)
        f.close()
    except:
        print("Il y a eu une erreur lors du téléchargement de la liste des jeux.")
        print("Si il y un probleme, un bug, ou si vous voulez des renseignements, contactez moi à : nathpython@gmail.com")
    if "data.nath" in os.listdir(direm):
        f=open(direm+"data.nath","r").read().split(cc)
        for ff in f:
            if ff not in [""," ","\b","'b"]:jeux.append( ff.split(c) )
    else:
        print("Il y a eu une erreur, veuillez réessayer ultérieurement.")
        print("Si il y un probleme, un bug, ou si vous voulez des renseignements, contactez moi à : nathpython@gmail.com")
    print("")
    print("#################################################################")
    print("")
    print("Jeux disponibles : ")
    print("")
    for j in jeux: 
        print(" "+str(jeux.index(j)+1)+"-"+str(j[0]))
    print("")
    print(" q-menu principal")
    choix=inp(" : ")
    if choix!="q":
        try:
            choix=int(choix)-1
            if choix>=0 and choix < len(jeux):
                page_jeu_magasin(jeux[choix])
            else:
                print("Vous ne pouvez faire cela.")
        except: print("Vous ne pouvez faire cela.")
        magasin()
        
        
    


def bibliotheque():
    jeux=[]
    for o in os.listdir(direj): jeux.append(o)
    print("")
    print("#################################################################")
    print("")
    print("Vos jeux : ")
    print("")
    for j in jeux:
        print(" "+str(jeux.index(j)+1)+"-"+j)
    print("")
    print(" q-revenir au menu")
    choix=inp(" : ")
    if choix!="q":
        bibliotheque()
    


def menu():
    print("")
    print("#################################################################")
    print("")
    print("Vous êtes dans le menu principal, que voulez vous faire ?")
    print(" 1-voir mes jeux installés")
    print(" 2-voir les jeux disponibles")
    print(" q-quitter")
    choix=inp(" : ")
    if choix == "1": bibliotheque()
    elif choix == "2": magasin()
    elif choix == "q": exit()
    menu()

menu()



