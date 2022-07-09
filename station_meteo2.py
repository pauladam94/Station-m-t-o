#import serial
import os 
import numpy as np
import pylab as plt
from time import sleep
from random import randint
import matplotlib.animation as animation


## fonction d'afichage
def animate(i):
    values.append(values.pop(0))
    line.set_ydata(values)
    return(line)

##on definit une fonction qui épure les données brut de 
##l'arduino
def pur(liste):
    # Ces trois  instructions fonctionnent, la seconde a ma préférence
    # return [mes[2:][:-2] for mes in liste]
    return [mes[2:].strip('\n').strip('\r')  for mes in liste]
    # return [mes.strip('b').strip('\'').strip(',').strip('\n').strip('\r')   for mes in liste]

##fonction pour enregistrer definitivement dans un fichier
##texte (.txt) les données venant de l'arduino
def write(L):
    file=open(os.path.join(os.path.dirname(__file__),"data.txt"),mode="w")
    for mes in L:
        file.write(f'{mes}\n')
    file.close()

##on definit la fonction mo qui fait la 
##moyennne des termes d'une liste (pour reg_lin)
def mo(p):
    return(sum(p)/len(p))

##regression linéaire pour les trois derniers points 
##des listes"""
def reg_lin(lx,ly):
    lxc=[(i)**2 for i in lx]
#on définit la liste des couple x*y
    lxy=[x*y for x,y in zip(lx,ly)]

# cacule de m et p dans y = m * x + p
    m=(mo(lx)*mo(ly)-(mo(lxy)))/((mo(lx)**2)-mo(lxc))
    p=(mo(lx)*mo(lxy)-(mo(ly)*mo(lxc))) / (((mo(lx))**2)-mo(lxc))

##affichage des points et de la droite 
#    xlim(min(lx)-2,max(lx)+2)
#    ylim(min(ly)-2,max(ly)+2)
#    title("Régression linéaire d'un nuage de point :")
#    xlabel(nm_abscisse)si utilisé rajouter deux parametres
#    ylabel(nm_ordonnée) deux parametres à la fonction
#    scatter(lx,ly,s=25)
#    x=linspace(0,300,300)
#    y=m*x+p
#    plt.plot(x,y)
#    plt.show()
    m=round(m,2)
    p=round(p,2)
#    print("y =",m,"*x+",p)
    return(m,p)

##fonction principale du programme

def station_meteo():
    plt.close()
## essai
#    try:
#        global (arduino) = serial.Serial ("???????????/dev/ttyACM0", timeout=1)
#    except:
#        print("verifier le port utilisé")
#    databrut=[]
#    compt=0

## essai
#   while True:
#       print(str(arduino.readline))

# brutdata=["b,234;1\r\n","b'122;2\r\n","b'123;3\r\n","b,324;4\r\n","b,324;5\r\n","b,324;6\r\n","b,324;7\r\n","b,324;8\r\n","b,324;9\r\n","b,324;10\r\n",]
#    while compt<4:
#        brutdata.append(str(arduino.readline))
#        compt+=1


    cleandata=pur(brutdata)

#   L=["234;1","122;2","123;3","324;4"]
#   write(L)
    write(cleandata)
    val,temp=np.loadtxt(os.path.join(os.path.dirname(__file__),"data.txt"),delimiter=";",unpack=True)
    
    
#   plt.xlim(min(lx)-2,max(lx)+2)
#   plt.ylim(min(ly)-2,max(ly)+2)
    plt.plot(temp,val,"o-",label="ligne -")
    (m,p)=reg_lin(temp[-3:],val[-3:])
    x=plt.linspace(min(temp[-3],temp[-2],temp[-1]),max(temp)+1,max(temp)+1)
    y = m*x+p
    a=max(temp)+1
    plt.scatter(a,a*m+p,s=30)
    plt.plot(x,y)
    
    
#    fig,ax=plt.subplots()
#    values=
#    line=ax.plot(x[:count],values)
    
    
#    ani=animation.FuncAnimation(fig,animate,interval=100)
    plt.show()
    sleep(1)
    brutdata.append("b'"+str(randint(0,1000))+";"+str(max(temp)+1)+"\b\r")

## boucle infini pour faire tourner en continu le programme

brutdata=["b,234;1\r\n","b'122;2\r\n","b'123;3\r\n","b,324;4\r\n","b,424;5\r\n","b,489;6\r\n","b,543;7\r\n","b,654;8\r\n","b,344;9\r\n","b,124;10\r\n",]
station_meteo()















