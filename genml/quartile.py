from math import ceil


def calculDesQuartiles(self, mediane, rangMediane):
    n = self.feature.count()
    sort_feature = self.feature.sort_values()
    sort_feature = sort_feature.reset_index(drop=True)
    q1 = 0
    q2 = mediane
    q3 = 0

    #Calcul Q1
    resteDivision = rangMediane%2
    if(resteDivision != 0):
        q1 = sort_feature[((rangMediane/2)+1)-1]
    else:
        valeurMin = sort_feature[((rangMediane/2)-1)]
        valeurMax = sort_feature[(rangMediane/2)]
        q1 = (valeurMin + ((valeurMax-valeurMin)/2)+ valeurMax) / 2

    
    #Calcul Q3
    nbdonnees = len(sort_feature)+1
    nbDonneesDepuisMediane = nbdonnees - rangMediane
    resteDivision = nbDonneesDepuisMediane % 2 
    if (resteDivision != 0):
        q3 = sort_feature[(rangMediane+ceil(nbDonneesDepuisMediane/2))-1]
    else:
        valeurMinQ3 = sort_feature[(rangMediane+(nbDonneesDepuisMediane/2))-1]
        valeurMaxQ3 = sort_feature[(rangMediane+(nbDonneesDepuisMediane/2))]
        q3 = (valeurMinQ3 + ((valeurMaxQ3 - valeurMinQ3)/2)+ valeurMaxQ3) / 2 
    
    return ([q1,q2,q3])
