#import serial (telecharger le module)
from fct_station_meteo import *
import numpy as np
import pylab as plt
from time import sleep
from random import randint
import matplotlib.animation as animation

## boucle infini pour faire tourner en continu le programme
b=0
brutdata=["b,234;1\r\n","b'122;2\r\n","b'123;3\r\n","b,324;4\r\n","b,424;5\r\n","b,489;6\r\n","b,543;7\r\n","b,654;8\r\n","b,344;9\r\n","b,124;10\r\n",]

a=int(input("Courbe de température(1), Courbe de luminosité(0) :")
if a = 1 :
    while b<5:    
        station_meteo("station météo : température")
        sleep(2)
        b+=1
if a = 0 :
    while b>5:
        station_meteo("station météo : température")
        sleep(2)
        b+=1
plt.show()














