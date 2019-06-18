#coding:utf-8
#launcher texte
import os,sys
import requests
import zipfile
import shutil
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
    jdt=False
    nmj=False
    version_i=""
    try:
        req = requests.get(jeu[4])
        for chunk in req.iter_content(1000):  version_i+=str(chunk)
    except: print("ERREUR : N'arrive pas à accéder à la dernière version du jeu")
    if jeu[0] in os.listdir(direj):
        jdt=True
        version_p=open(direj+jeu[0]+"/version","r").read()
        if version_p!=version_i: nmj=True
    print("")
    print("#################################################################")
    print("")
    print("Voici la page du jeu "+str(jeu[0]))
    print("")
    print("dernière version : "+version_i)
    if jdt: print("version téléchargée : "+version_p)
    print("")
    print("description : "+str(jeu[2]))
    print("")
    if not jdt : print(" 1-télécharger le jeu")
    elif jdt and nmj:
        print(" 1-Le jeu n'est pas mis à jour, METTRE A JOUR LE JEU")
    else:
        print(" 1-Le jeu est déjà installé et mis à jour")
    print(" q-menu précédent")
    choix=inp(" : ")
    if choix!="q":
        if choix=="1" and (not jdt or nmj):
            print("Téléchargement du jeu :")
            try:
                print(" .requete de l'url..")
                url=jeu[1]
                req = requests.get(url)
                print(" .telechargement du fichier zip...")
                txxt=b''
                for chunk in req.iter_content(1000):
                    txxt+=chunk
                f=open(direj+jeu[0]+".zip","wb")
                f.write(txxt)
                f.close()
                print(" .extraction du fichier zip...")
                zip_ref = zipfile.ZipFile(direj+jeu[0]+".zip","r")
                zip_ref.extractall(direj+jeu[0]+"/")
                zip_ref.close()
                print(" .netoyage des fichiers inutiles...")
                os.remove(direj+jeu[0]+".zip")
                print(" .arrangement des fichiers...")
                df1=direj+jeu[0]+"/"+jeu[0]+"-master/"
                df2=direj+jeu[0]+"1/"
                df3=direj+jeu[0]+"/"
                os.rename(df1,df2)
                os.rmdir(df3)
                os.rename(df2,df3)
                print("Jeu téléchargé.")
            except:
                print("ERREUR : Il y a eu une erreur lors du téléchargement du jeu.")
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
            if ff not in [""," ","\b","'b","b''",'b"']:jeux.append( ff.split(c) )
    else:
        print("ERREUR : Il y a eu une erreur, veuillez réessayer ultérieurement.")
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
        except: print("ERREUR : Vous ne pouvez faire cela.")
        magasin()

def calc_taille_dossier(dj,taille):
    for o in os.listdir(dj):
        if os.path.isfile(dj+"/"+o):
            statinfo = os.stat(dj+"/"+o)
            taille+=statinfo.st_size
        else:
            taille=calc_taille_dossier(dj+"/"+o+"/",taille)
    return taille

def page_jeu_b(dj):
    taille=calc_taille_dossier(dj,0)
    nom=dj.split("/")[len(dj.split("/"))-1]
    print("")
    print("#################################################################")
    print("")
    print("Page du jeu : "+nom)
    print("")
    if len(str(taille)) >= 9: print("taille : "+str(taille/10**9)+" Go")
    elif len(str(taille)) >= 6: print("taille : "+str(taille/10**6)+" Mo")
    elif len(str(taille)) >= 3: print("taille : "+str(taille/10**3)+" Ko")
    else: print("taille : "+str(taille)+" o")
    print("")
    print(" 1-jouer au jeu")
    print(" 2-désinstaller le jeu")
    print(" 3-voir la page du jeu du magasin")
    print(" q-quitter")
    choix=inp(" : ")
    if choix!="q":
        if choix=="1": os.system("cd "+str(dj)+"&& python main.py")
        if choix=="2":
            print("")
            print("Etes vous vraiment sur de supprimer ce jeu ? (Y/N)")
            choix2=inp(" : ")
            if choix2=="Y":
                print("Désinstallation du jeu...")
                shutil.rmtree(dj)
                os.rmdir(dj)
        if choix=="3":
            if "data.nath" in os.listdir(direm):
                jex=[]
                jj=None
                f=open(direm+"data.nath","r").read().split(cc)
                for ff in f:
                    if ff not in [""," ","\b","'b","b''",'b"']:jex.append( ff.split(c) )
                for j in jex:
                    if j[0]==nom: jj=j
                if jj!=None: page_jeu_magasin(jj)
                else: print("ERREUR : Ne peut pas accéder à la page du jeu du magasin")
            else: print("ERREUR : Ne peut pas accéder à la page du jeu du magasin")
        if choix not in ["2"]: page_jeu_b(dj)

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
        if True:
            choix=int(choix)-1
            if choix>=0 and choix < len(jeux):
                page_jeu_b(direj+jeux[choix])
            else:
                print("Vous ne pouvez faire cela.")
        else: print("Vous ne pouvez faire cela.")
        bibliotheque()
    


def menu():
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
        print("ERREUR : Il y a eu une erreur lors du téléchargement de la liste des jeux.")
        print("Si il y un probleme, un bug, ou si vous voulez des renseignements, contactez moi à : nathpython@gmail.com")
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



