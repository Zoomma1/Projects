import matplotlib.pyplot as plt
from random import *
import numpy as np
from matplotlib.colors import ListedColormap


dens=0.4 #Densité de vehicules sur la route
taille_route=17500 #taille de la route(1 unité = 1 voiture et 1 case environ= 2 metres)
vmax=5 #vitesse max de la voiture (x unité de vitesse = X unité de deplacements de la voiture a i+1 si possible)
t=1000 #nombres d'iterations
nb_voitures=int(dens*taille_route)
p=0.06
#route=[voiture,vitesse]

####################################################################
#Creation route                                                    #
####################################################################


def crea_route(dens,nb_voitures):
    route=[[0,0]]*nb_voitures + [[-1,0]]*(taille_route-nb_voitures)
    shuffle(route)
    return route


####################################################################
#Creation d'une liste de distance entre les vehicules              #
####################################################################

		
def dist(route):
	dist = []
	for i in range(taille_route):
		if route[i][0] > -1:
			d = 1
			while route[(i + d) % taille_route][0] < 0:
				d += 1
			dist.append(d)
	return dist
	

####################################################################
#aceleration des vehicules                                         #
####################################################################


def accel(route):
	for i in range(len(route)):
		if route[i][0] > -1 and route[i][0] < vmax:
			route[i][0] += 1
	return route


####################################################################
#deceleration des vehicules                                        #
####################################################################


def decel(route,dist):
	k = 0
	routet=[[-1,0] for i in range(taille_route)]
	for i in range(taille_route):
		if route[i][0] > -1:
			routet[i][0] = min(route[i][0], dist[k] - 1)
			k += 1
	return routet
	
	
def decelerationalea(route: list) -> list:
    for i in range(taille_route):
        if route[i][0] > 0 and random() < p:
            route[i][0] += -1
    return route

####################################################################
#Mouvement                                                         #
####################################################################


def mvt(route):
	routet=[[-1,0] for i in range(taille_route)]
	for i in range(taille_route):
		if route[i][0]>-1:
			routet[(i + route[i][0]) % taille_route] = route[i]
	return routet
	


####################################################################
#Main                                                              #
####################################################################	

def main(dens,nb_voitures):
    route=crea_route(dens,nb_voitures)
    resultats=[route]
    for i in range(t):
    	dis=dist(route)
    	route=accel(route)
    	route=decel(route,dis)
    	route=decelerationalea(route)
    	route=mvt(route)
    	resultats.append(route)
    	perc = ((t - (t - i)) / t) * 100
    	if perc % 5 == 0: print(perc, '%')
    	
    a = np.zeros(shape=(t, taille_route))
    for i in range(taille_route):
        for j in range(t):
            a[j, i] = resultats[j][i][0]*(200) if resultats[j][i][0] > -1 else None
    cmap= 'RdYlGn'
    plt.xlabel("Distance")
    plt.ylabel("Temps")
    plt.imshow(a, cmap,interpolation="nearest")
    plt.show()
    return route	

main(dens,nb_voitures)


