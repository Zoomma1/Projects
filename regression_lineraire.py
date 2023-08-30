import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# variables d'entrées
# =============================================================================
np.random.seed(0)
n_echantillion=100
nb_iterations=10
vitesse_apprentissage=0.1
x = np.linspace(0,10,n_echantillion).reshape((n_echantillion,1))
y = x + np.random.randn(n_echantillion,1)
X = np.hstack((x,np.ones(x.shape)))
theta=np.random.randn(2,1)

# =============================================================================
# definition des fonctions
# =============================================================================
def fonction(X,theta):
    return X.dot(theta)

def cout(X,y,theta):
    return (1/(2*len(y)))*np.sum((X.dot(theta)-y)**2)

def gradient(X,y,theta):
    return (1/(2*len(y)))*X.T.dot(fonction(X,theta)-y)

def desc_gradient(X,y,theta,vitesse_apprentissage,nb_iterations):
    historique_cout=np.zeros(nb_iterations)
    for i in range(nb_iterations):
        theta = theta-vitesse_apprentissage*gradient(X,y,theta)
        historique_cout[i]=cout(X,y,theta)
    return theta,historique_cout

# =============================================================================
# main
# =============================================================================
thetaf ,  historique_cout = desc_gradient(X,y,theta,vitesse_apprentissage,nb_iterations)
print(thetaf)
predictions = fonction(X, thetaf)
plt.scatter(x, y)
plt.plot(x, predictions, c='r')
plt.show()
plt.plot(range(nb_iterations), historique_cout)
plt.show()
