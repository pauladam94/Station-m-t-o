# Station-meteo

Ce projet est différents des autres car fait intervenir une carte arduino. L'objectif est de créer
une petite station météo. Avec une carte arduino qui récupère la luminosité et la température, 
j'ai souhaité faire des prévisions de météo et un affichage de ces informations. Il a été 
intéressant de travailler à récupérer de manière efficace les données de l'Arduino depuis un 
programme python.
Les prévisions sont faites simplement par des régressions linéaires sur les dernières valeurs 
obtenus.
