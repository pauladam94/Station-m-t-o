import serial
import numpy as np
import pylab as plt
from time import sleep
from random import randint
import matplotlib.animation as animation

##on definit une fonction qui épure les données brut de
##l'arduino
def pur(liste):
    newliste=[]
    for i in range(len(liste)):
        a=liste[i][2:]
        newliste.append(a[:-2])
    return(newliste)


##fction pour enregistrer definitivement dans un fichier
##texte (.txt) les données venant de l'arduino
def write(L):
    file=open("data.txt",mode="w")
    for i in range(len(L)):
        file.write(L[i]+'\n')
    file.close()


##on definit la fonction mo qui fait la
##moyennne des termes d'une liste (pour reg_lin)
def mo(p):
    return(sum(p)/len(p))


##regression linéaire pour les trois derniers points
##de la courbe
def reg_lin(lx,ly):
    lx=[lx[-3],lx[-2],lx[-1]]
    ly=[ly[-3],ly[-2],ly[-1]]
#on définit la liste des x**2
    lxc=[(i)**2 for i in lx]

#on définit la liste des couple x*y
    lxy=[x*y for x,y in zip(lx,ly)]

# cacule de m et p dans y = m * x + p
    m=(mo(lx)*mo(ly)-(mo(lxy)))/((mo(lx)**2)-mo(lxc))
    p=(mo(lx)*mo(lxy)-(mo(ly)*mo(lxc))) / (((mo(lx))**2)-mo(lxc))
    m=round(m,2)
    p=round(p,2)
    return(m,p)

##fonction principale du programme
def station_meteo(nom_graphique,nom_axe_ordonnee):
    plt.close()

## essai :
#    try:
#        global (arduino) = serial.Serial ("???????????/dev/ttyACM0", timeout=1)
#    except:
#        print("verifier le port utilisé")
#    databrut=[]
#    compt=0

## essai :
#   while True:
#       print(str(arduino.readline))


## tres important
#    while compt<4:
#        brutdata.append(str(arduino.readline))
#        compt+=1
    cleandata=pur(brutdata)
    write(cleandata)
    val,temp=np.loadtxt("data.txt",delimiter=";",unpack=True)
#   plt.xlim(min(lx)-2,max(lx)+2)
#   plt.ylim(min(ly)-2,max(ly)+2)
    plt.plot(temp,val,"o-",label="ligne -")
    (m,p)=reg_lin(temp,val)
    x=plt.linspace(min(temp[-3],temp[-2],temp[-1]),max(temp)+1,max(temp)+1)
    y = m*x+p
    a=max(temp)+1
    plt.scatter(a,a*m+p,s=30)
    plt.plot(x,y)


##affichage des points et de la droite
    plt.xlim(min(lx)-2,max(lx)+2)
    plt.ylim(min(ly)-2,max(ly)+2)
    plt.title(nom_graphique)
    plt.xlabel("temps(en s)")
    plt.ylabel(nom_axe_ordonnee)
    brutdata.append("b'"+str(randint(0,1000))+";"+str(max(temp)+1)+"\b\r")
#    scatter(lx,ly,s=25)
#    x=linspace(0,300,300)
#    y=m*x+p
#    plt.plot(x,y)


## boucle infini pour faire tourner en continu le programme
b=0
brutdata=["b,234;1\r\n","b'122;2\r\n","b'123;3\r\n","b,324;4\r\n","b,424;5\r\n","b,489;6\r\n","b,543;7\r\n","b,654;8\r\n","b,344;9\r\n","b,124;10\r\n",]

a=int(input("Courbe de température(1), Courbe de luminosité(0) :"))

if a == 1 :
    while b<5:
        station_meteo("station météo : température")
        sleep(2)
        b+=1

if a == 0 :
    while b>5:
        station_meteo("station météo : température")
        sleep(2)
        b+=1
plt.show()