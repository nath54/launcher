#coding:utf-8
#!/bin/python3

import os,sys
try:
    import requests
except:
    print("La librairie requests va etre installée sur votre ordinateur")
    os.system("pip install requests")
    import requests
try: import zipfile
except:
    print("La librairie zipfile va etre installée sur votre ordinateur")
    os.system("pip install zipfile")
    import zipfile
try: import shutil
except:
    print("La librairie shutil va etre installée sur votre ordinateur")
    os.system("pip install shutil")
    import shutil
try: import subprocess
except:
    print("La librairie subprocess va etre installée sur votre ordinateur")
    os.system("pip install subprocess")
    import subprocess
from os.path import expanduser
home = expanduser("~")

direlauncher="Launcher/"
direjeux="jeux/"
if not direlauncher[:-1] in os.listdir(home):
    os.mkdir(home+"/"+direlauncher)
    os.mkdir(home+"/"+direlauncher+direjeux)
direm=home+"/"+direlauncher
if not direjeux[:-1] in os.listdir(direm):
    os.mkdir(home+"/"+direlauncher+direjeux)
direj=home+"/"+direlauncher+direjeux

def inp(txt):
    vp=sys.version_info
    if vp[0]==2: return raw_input(txt)
    else: return input(txt)

fp="params.nath"
lll=[]
if not fp in os.listdir(direm):
    for ll in os.listdir("data/"):
        if ll[-5:]==".nath": lll.append(ll)
    print("Wich language do you want ? ")
    for l in lll:
        print("    "+str(lll.index(l))+"-"+l.split("_") [1])
    choix=inp(" : ")
    try:
        i=int(choix)
        l=lll[i]
    except:
        print("ERROR : the default language is chosen")
        l=lll[0]
    f=open(direm+fp,'w')
    f.write(l)
    f.close()

f=open(direm+fp,"r").read()
tl=open("data/"+f,"r",encoding="utf-8").read().split("\n")

c="#"
cc="|"
ccc=","

vp=sys.version_info
if vp[0]==2:
    print(tl[44])
    inp("")

for o in os.listdir(direj):
    if o[-1]=="1":  shutil.rmtree(direj+o)

version_actuelle=float(str(open("version","r").read().replace("\n","")))
urlv="https://raw.githubusercontent.com/nath54/launcher/master/version"
dv=""
req = requests.get(urlv)
for chunk in req.iter_content(1000):  dv+=str(chunk,"utf-8")
try:
    dv=float(str(dv.replace("\n","")))
except: dv=0

print(tl[51]+str(version_actuelle))
print(tl[52]+str(dv))
if version_actuelle < dv: print(tl[53])
else: print(tl[54])
inp(">")

def page_jeu_magasin(jeu,tl):
    jdt=False
    nmj=False
    version_i=""
    try:
        req = requests.get(jeu[4])
        for chunk in req.iter_content(1000):  version_i+=str(chunk,"utf-8")
        version_i=str(version_i.replace("\n",""))
    except: print(tl[0])
    if jeu[0] in os.listdir(direj):
        jdt=True
        version_p=open(direj+jeu[0]+"/version","r").read()
        version_p=str(version_p.replace("\n",""))
        if version_p!=version_i: nmj=True
    print("")
    print("#################################################################")
    print("")
    print(tl[1]+str(jeu[0]))
    print("")
    print(tl[2]+version_i)
    if jdt: print(tl[3]+version_p)
    print("")
    print(tl[4]+str(jeu[2]))
    print("")
    if not jdt : print(tl[5])
    elif jdt and nmj:
        print(tl[6])
    else:
        print(tl[7])
    print(tl[8])
    choix=inp(" : ")
    if choix!="q":
        if choix=="1" and (not jdt or nmj):
            print(tl[9])
            try:
                print(tl[10])
                if jeu[0] in os.listdir(direj): shutil.rmtree(direj+jeu[0])
                if jeu[0]+"1" in os.listdir(direj): shutil.rmtree(direj+jeu[0]+"1")
                print(tl[11])
                url=jeu[1]
                req = requests.get(url)
                print(tl[12])
                txxt=b''
                tt=0
                for chunk in req.iter_content(1000):
                    txxt+=chunk
                    tt+=len(chunk)
                if len(str(tt))>9: print(str(tt/10**9)+"Go")
                if len(str(tt))>6: print(str(tt/10**6)+"Mo")
                if len(str(tt))>3: print(str(tt/10**3)+"Ko")
                else: print(str(tt)+"o")
                f=open(direj+jeu[0]+".zip","wb")
                f.write(txxt)
                f.close()
                print(tl[13])
                zip_ref = zipfile.ZipFile(direj+jeu[0]+".zip","r")
                zip_ref.extractall(direj+jeu[0]+"/")
                zip_ref.close()
                print(tl[14])
                os.remove(direj+jeu[0]+".zip")
                print(tl[15])
                df1=direj+jeu[0]+"/"+jeu[0]+"-master/"
                df2=direj+jeu[0]+"1/"
                df3=direj+jeu[0]+"/"
                os.rename(df1,df2)
                os.rmdir(df3)
                os.rename(df2,df3)
                print(tl[16])
                print(tl[17])
                for r in jeu[3].split(','):
                    p=subprocess.Popen('python -c "import '+r+'"')
                    if p.returncode==0:
                        os.system("pip install "+r)
                    else: print(tl[18]+r+tl[19])
            except:
                print(tl[20])
        page_jeu_magasin(jeu,tl)

def magasin(tl):
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
        print(tl[21])
        print(tl[22])
    if "data.nath" in os.listdir(direm):
        f=open(direm+"data.nath","r").read().split(cc)
        for ff in f:
            if ff not in [""," ","\b","'b","b''",'b"']:jeux.append( ff.split(c) )
    else:
        print(tl[23])
        print(tl[22])
    print("")
    print("#################################################################")
    print("")
    print(tl[24])
    print("")
    for j in jeux: 
        print(" "+str(jeux.index(j)+1)+"-"+str(j[0]))
    print("")
    print(tl[25])
    choix=inp(" : ")
    if choix!="q":
        try:
            choix=int(choix)-1
            if choix>=0 and choix < len(jeux):
                page_jeu_magasin(jeux[choix],tl)
            else:
                print(tl[26])
        except: print(tl[27])
        magasin(tl)

def calc_taille_dossier(dj,taille):
    for o in os.listdir(dj):
        if os.path.isfile(dj+"/"+o):
            statinfo = os.stat(dj+"/"+o)
            taille+=statinfo.st_size
        else:
            taille=calc_taille_dossier(dj+"/"+o+"/",taille)
    return taille

def page_jeu_b(dj,tl):
    taille=calc_taille_dossier(dj,0)
    nom=dj.split("/")[len(dj.split("/"))-1]
    print("")
    print("#################################################################")
    print("")
    print(tl[28]+nom)
    print("")
    if len(str(taille)) >= 9: print(tl[29]+str(taille/10**9)+" Go")
    elif len(str(taille)) >= 6: print(tl[29]+str(taille/10**6)+" Mo")
    elif len(str(taille)) >= 3: print(tl[29]+str(taille/10**3)+" Ko")
    else: print(tl[29]+str(taille)+" o")
    print("")
    print(tl[30])
    print(tl[31])
    print(tl[32])
    print(tl[33])
    choix=inp(" : ")
    if choix!="q":
        if choix=="1":
            print("")
            print("##############################")
            print("")
            print(tl[55]+nom)
            print("")
            os.system("cd "+str(dj)+"&& python main.py")
            print("")
        if choix=="2":
            print("")
            print(tl[34])
            choix2=inp(" : ")
            if choix2=="Y":
                print(tl[35])
                shutil.rmtree(dj)
        if choix=="3":
            if "data.nath" in os.listdir(direm):
                jex=[]
                jj=None
                f=open(direm+"data.nath","r").read().split(cc)
                for ff in f:
                    if ff not in [""," ","\b","'b","b''",'b"']:jex.append( ff.split(c) )
                for j in jex:
                    if j[0]==nom: jj=j
                if jj!=None: page_jeu_magasin(jj,tl)
                else: print(tl[36])
            else: print(tl[36])
        if choix not in ["2"]: page_jeu_b(dj,tl)

def bibliotheque(tl):
    jeux=[]
    for o in os.listdir(direj): jeux.append(o)
    print("")
    print("#################################################################")
    print("")
    print(tl[37])
    print("")
    for j in jeux:
        print(" "+str(jeux.index(j)+1)+"-"+j)
    print("")
    print(tl[38])
    choix=inp(" : ")
    if choix!="q":
        try:
            choix=int(choix)-1
            if choix>=0 and choix < len(jeux):
                page_jeu_b(direj+jeux[choix],tl)
            else:
                print(tl[39])
        except: print(tl[39])
        bibliotheque(tl)

def parametres(tl):
    print("")
    print("#################################################################")
    print("")
    print(tl[46])
    print(tl[47])
    print(tl[48])
    choix=inp(" : ")
    if choix!="q":
        if choix=="1":
            lll=[]
            for ll in os.listdir("data/"):
                    if ll[-5:]==".nath": lll.append(ll)
            print(tl[49])
            for l in lll:
                print("    "+str(lll.index(l))+"-"+l.split("_") [1])
            choix=inp(" : ")
            try:
                i=int(choix)
                l=lll[i]
            except:
                print(tl[50])
                l=lll[0]
            f=open(direm+fp,'w')
            f.write(l)
            f.close()
            f=open(direm+fp,"r").read()
            tl=open("data/"+f,"r",encoding="utf-8").read().split("\n")
        tl=parametres(tl)
    return tl

def menu(tl):
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
        print(tl[21])
        print(tl[22])
    print("")
    print("#################################################################")
    print("")
    print(tl[40])
    print(tl[41])
    print(tl[42])
    print(tl[45])
    print(tl[43])
    choix=inp(" : ")
    if choix == "1": bibliotheque(tl)
    elif choix == "2": magasin(tl)
    elif choix == "3": tl=parametres(tl)
    elif choix == "q": exit()
    menu(tl)

menu(tl)



