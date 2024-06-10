import os
import time
import copy
import sys

SYMBOLE1 = input("quelle est le symbole de la cellule en vie ")
SYMBOLE0 = input("quelle est le symbole de la cellule en morte ")
#Demande à l'utilisateur quel symbole veut-il mettre pour l'affichage

t1 = [[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
t2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
t3 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
t4 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
t5 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
tableau = [t1,t2,t3,t4,t5]
# L'ensemble des tableaux pré-enregistrer dans la liste tableau

class JeuDeLaVie:
    
    def __init__(self, tableau):
        """
        Affecte un tableau à deux dimensions à l’attribut tableau

        :param tableau: tableau à deux dimensions
        """
        self.tableau = tableau
        
    def affichage(self):
        """
        fait afficher le tableau dans le shell

        """
        os.system('cls')                            #Efface le tableau précédent
        
        for i in range (len(self.tableau)):
            for j in range (len(self.tableau)-1):   # Fait 2 boucles afin d'écrire chaque valeur du taleau
                if self.tableau[i][j] == 0:         #Si la valeur est 0. La fonction le remplace par un symbole définie par l'utilisateur
                    print(SYMBOLE0, end='')
                else:                               #Sinon elle le remplace par l'autre symbole définie par l'utilisateur
                    print(SYMBOLE1, end='')
            if self.tableau[i][j+1] == 0:           #Renvoie la dernière valeur de la ligne puis passe à la ligne suivante
                print(SYMBOLE0)
            else:
                print(SYMBOLE1)
        
    def run(self, nombre_tours, delai):
        """
        Méthode principale du jeu.

        Fait tourner le jeu de la vie pendant nombre_tours.
        Elle rafraichit l’affichage à chaque tour
        et attend delai entre chaque tour.
        Vérifie si le tableau actuelle est le même que celui précédement

        :param nombre_tours: nombre de tours à effectuer
        :param delai: temps d’attente en secondes entre chaque tour
        """
        for a in range(nombre_tours):
            time.sleep(delai)                   #Le temps entre chaque apparition du tableau
            b = copy.deepcopy(self.tableau)     #Fais une copy du tableau
            self.tour()                         #Actualise le tableau
            self.affichage()                    #Puis l'affiche
            if self.tableau == b:               #Si le tableau = le tableau précédent
                time.sleep(2.5)
                lancement()                     #Le programme reviens au début à l'achèvement
        time.sleep(2.5)
        lancement()
        
    def tour(self):
        """
        Met à jour toute les cellules du tableau en respectant les règles
        du jeu de la vie.
        Pour cela on utilise les fonctions ci-dessous pour déterminer les valeurs 
        que doit prendre le tableau
        """
        x = copy.deepcopy(self.tableau)     #Fait une copy indépendante du tableau dans X
        for i in range(len(x)):
            for j in range(len(x)):
                self.tableau[i][j] = self.resultat(self.valeur_case(i,j),self.total_voisins(i,j))
        #Actualise le tableau 
    
    def valeur_case(self, i, j):
        """
            Renvoie la valeur de la case [i][j] ou 0 si la case n’existe pas.
            On vérifie si les valeurs sont dans le tableau
        """
        if 0 <= i <= int(len(self.tableau)-1) and 0 <= j <= int(len(self.tableau[i])-1) : #vérifie si la valeur est dans le tableau
            return self.tableau[i][j]           #Renvoie la valeur de la case                                                        
        else:                                   #La case est en dehors du tableau
            return 0                            #On renvoie 0
        
    def total_voisins(self, i, j):
        """Renvoie la somme des valeurs des voisins de la case [i][j].
        On créer 2 boucles qui vont prendre la somme des valeurs des cases autour d'elle
        puis renvois la somme
        
        """  
        somme = 0
        for l in range(-1,2):
            for k in range(-1,2):                   #créer 2 boucles qui vont prendre les coordonnées des voisins de la case [i][j]
                somme += self.valeur_case(i+l,j+k)  #calcul la somme dans somme de la valeur des voisins
        somme -= self.valeur_case(i,j)              #retire la valeur de la case [i][j]
        return somme                                #Ensuite la fonction retourne le nombre de voisin
                    
    def resultat(self, valeur_case, total_voisins):
        """
        Renvoie la valeur suivante d’une la cellule.
        on entre toute les règles du jeu
        :param valeur_case: la valeur de la cellule (0 ou 1)
        :param total_voisins: la somme des valeurs des voisins
        :return: la valeur de la cellule au tour suivant

        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 3)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 1)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 4)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 2)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 3)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 1)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 4)
        0
        """
        if valeur_case == 0:                    #vérifie la valeur de la case et si la valeur = 0
            if total_voisins == 3:              #vérifie si son nombre de voisin est de 3
                return 1                        # Puis retourne la valeur qu'elle doit avoir
            else :
                return 0
        else :                                  #la fonction refait la même chose mais avec une valeur de 1
            if total_voisins == 2 or total_voisins == 3 :
                return 1
            else :
                return 0

def lancement ():
    """
    commande de départ qui permet à l'utilisateur de naviguer entre les fonctions ci-dessous
    - créer un tableau
    - afficher les tableaux pré-enregistrer
    - démarer le jeu de la vie
    Permet d'être rappeler après avoir afficher les tableaux pré-enregistrer
    """
    os.system('cls')
    print("Choisissez un tableau pré-enregistré entre 1 et ",len(tableau))
    print("Sinon entrez ",len(tableau)+1," pour afficher les tableaux pré-enregistrer")
    print("Ou alors entrez ",len(tableau)+2,end = ' ' )
    commande = int(input("pour mettre fin  "))
    if commande == len(tableau)+1 :
        for v in range(1,len(tableau)+1):
            os.system('cls')
            print("Le tableau numéro",v," est :")
            affiche_tab(v-1)
            input()
        lancement()
    elif commande == len(tableau)+2 :
        print("Au revoir, à bientôt")               
        time.sleep(2.5)
        os.system('cls')                #efface ce qui est afficher à l'écran
        sys.exit()                      #Et ferme la fenêtre
    else :
        for y in range(1,len(tableau)+1):               #boucle qui va lancer le tableau sélectionner
            if y == commande:                           #séléctionner par l'utilisateur
                mon_jeu = JeuDeLaVie(tableau[y-1])      #entre le tableau dans la fonction objet
                mon_jeu.run(100,0.2)                    #Puis lance le jeu

def affiche_tab (T):
    """
    fais afficher les différents tableaux pré-enregistrer dans le schell
    ----------
    T : TYPE int
    variable qui représente chaque élément de la liste tableau
    """
    d = copy.deepcopy(tableau[T])   #fais une copy indépendante d'une valeur du tableau avec les tableaux pré-enregistrer
    for i in range (len(d)):
        for j in range (len(d)-1):   # Fait 2 boucles afin d'écrire chaque valeur du taleau
            if d[i][j] == 0:         #Si la valeur est 0. La fonction le remplace par un symbole définie par l'utilisateur
                   print(SYMBOLE0, end='')
            else:                               #Sinon elle le remplace par un autre symbole définie par l'utilisateur
                   print(SYMBOLE1, end='')
        if d[i][j] == 0:           #Renvoie la dernière valeur de la ligne puis passe à la ligne suivante
               print(SYMBOLE0)
        else:
               print(SYMBOLE1)

lancement()    #appelle la fonction prerequis pour commencer le programme