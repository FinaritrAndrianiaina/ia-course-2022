"""
    La régression linéaire
    La régression linéaire multiple est une méthode ancienne de statistique mais qui trouve encore de nombreuses applications aujourd'hui. Que ce soit pour la compréhension des relations entre des variables ou pour la prédiction, cette méthode est en général une étape quasi obligatoire dans toute méthodologie data science.

    Le principe de la régression linéaire : il consiste à étudier les liens entre une variable dépendante et des variables indépendantes. La régression permet de juger de la qualité d'explication de la variable dépendante par les variables indépendantes.

    Le modèle statistique sous-jacent est très simple, il s'agit d'une modèle linéaire qui est généralement écrit :
    y=constante + beta1 x1 + beta2 x2 + ... + erreur

    L'estimation des paramètres de ce modèle se fait par l'estimateur des moindres carrés et la qualité d'explication est généralement évalué par le R².

    La qualité de prédiction est généralement mesurée avec le RMSE (racine de la somme des carrés des erreurs).
"""

#Importation des données
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importation Modele
from sklearn.linear_model import LinearRegression

#importer les données Advertising.csv
donnees = pd.read_csv('Advertising.csv', index_col=0)
donnees.head()

#Créer le modèle
#créer un objet reg lin
modeleReg=LinearRegression()

#créer y et X
list_var=donnees.columns.drop("Sales")
y=donnees.Sales
X=donnees[list_var]

modeleReg.fit(X,y)

print(modeleReg.intercept_)
print(modeleReg.coef_)

#Affichage modèle
#calcul du R²
modeleReg.score(X,y)

RMSE=np.sqrt(((y-modeleReg.predict(X))**2).sum()/len(y))

plt.plot(y, modeleReg.predict(X),'.')
plt.show()

plt.plot(y, y-modeleReg.predict(X),'.')
plt.show()