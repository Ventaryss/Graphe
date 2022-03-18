# Créé par vince, le 16/03/2022 en Python 3.7

import random

#relier la reine à ses cases qu'elle menace

"""
Une classe Python pour creer et manipuler des graphes
"""

class Graphe(object):
    def __init__(self, graphe_dict=None):
        """ initialise un objet graphe.
            Si aucun dictionnaire n'est
            créé ou donné, on en utilisera un vide
        """
        if graphe_dict == None:
            graphe_dict = {}
        self._graphe_dict = graphe_dict

    def aretes(self, sommet):
        """ retourne une liste de toutes les aretes d'un sommet """
        if ((sommet in self._graphe_dict)==True):
            return self._graphe_dict[sommet]
        else:
            return "Erreur, le sommet n'est pas dans le graphe"

    def all_sommets(self):
        """ retourne tous les sommets du graphe """
        liste_sommets=[]
        for s in (self._graphe_dict.keys()):
            liste_sommets.append(s)
        return liste_sommets

    def all_aretes(self):
        """ retourne toutes les aretes du graphe
        à partir de la méthode privée,_list_aretes, à définir
        plus bas.
        Ici on fera donc simplement appel à cette méthode.
        """
        return self.__list_aretes()

    def add_sommet(self, sommet):
        """ Si le "sommet" n'est pas déjà présent
        dans le graphe, on rajoute au dictionnaire
        une clé "sommet" avec une liste vide pour valeur.
        Sinon on ne fait rien.
        """
        if sommet not in self._graphe_dict:
            self._graphe_dict[sommet]=set()
        else:
            print("Le sommet est déjà dans le graphe")

    def add_arete(self, arete):
        """ l'arete est de type set, tuple ou list;
        Entre deux sommets il peut y avoir plus
        d'une arete (multi-graphe)
        """
        if arete[0] not in self._graphe_dict or arete[1] not in self._graphe_dict:
            print("erreur, un des deux sommets n'est pas dans le graphe")
        else:
            self._graphe_dict[arete[0]].add(arete[1])
            self._graphe_dict[arete[1]].add(arete[0])


    def __list_aretes(self):
        """ Methode privée pour récupérers les aretes.
        Une arete est un ensemble (set)
        avec un (boucle) ou deux sommets.
        """
        liste=set()
        for i in self._graphe_dict:
            if self._graphe_dict[i]=={}:
                liste.add((i,' '))
            for j in self._graphe_dict[i]:
                liste.add((i,j))
        return liste

    def trouve_chaine(self, sommet_dep, sommet_arr, chain=None):
        if (chain==None):
            chain=[]
        chain.append(sommet_dep)

        if sommet_dep == sommet_arr:
            return chain

        for v in self._graphe_dict[sommet_dep]:
            if v not in chain:
                chaine = self.trouve_chaine(v,sommet_arr, chain)
                if chaine != []:
                    return chain
        chain.pop(len(chain)-1)
        return []

    def sommet_degre(self,sommet):
        """ renvoie le degre du sommet """
        return len(self._graphe_dict[sommet])

    def trouve_sommet_isole(self):
        """ renvoie la liste des sommets isoles """
        isoles=[]
        for  i in self._graphe_dict.keys():
            if  self.sommet_degre(i)==0:
                isoles.append(i)
        return isoles

    def list_degres(self):
        """ calcule tous les degres et renvoie un
        tuple de degres decroissant
        """
        degres=[]
        for i in self._graphe_dict.keys():
            degres.append(self.sommet_degre(i))
        degres.sort(reverse=True)
        return tuple(degres)

    def parcours_largeur(self, sommet_depart: str) -> list:
        """ Parcours en largeur du graphe
            @param : sommet de départ
            return : liste des sommets dans l'ordre du  parcours
        """
        f=[]
        f.append(sommet_depart)
        marque = [sommet_depart]
        resultat = Graphe()
        resultat.add_sommet(sommet_depart)

        while f != []:
            sommet_courant = f.pop(0)
            if sommet_courant not in marque:
                resultat.add_sommet(sommet_courant)

            for v in self._graphe_dict[sommet_courant]:
                if v not in marque:
                    marque.append(v)
                    f.append(v)
                    resultat.add_sommet(v)
                    resultat.add_arete([sommet_courant,v])
        return resultat

    def parcours_profondeur(self, sommet_depart: str) -> list:
        """ Parcours en profondeur du graphe
            @param : sommet de départ
            return : liste des sommets dans l'ordre du  parcours
        """
        p = []
        p.append(sommet_depart)
        marque=[sommet_depart]
        resultat = Graphe()
        resultat.add_sommet(sommet_depart)

        while p != []:
            sommet_courant = p.pop(len(p)-1)
            if sommet_courant not in marque:
                resultat.add_sommet(sommet_courant)

            for v in self._graphe_dict[sommet_courant]:
                if v not in marque:
                    marque.append(v)
                    p.append(v)
                    resultat.add_sommet(v)
                    resultat.add_arete([sommet_courant,v])
        return resultat

    def presence_cycle(self,sommet_depart):
        p = []
        p.append(sommet_depart)
        parent={}
        parent[sommet_depart] = ""

        while p != []:
            sommet_courant = p.pop(len(p)-1)
            for v in self._graphe_dict[sommet_courant]:
                if v != parent[sommet_courant]:
                    if v in parent:
                        return True
                    else:
                        parent[v]=sommet_courant
                        p.append(v)
        return False

    def presence_cycle_depart(self,sommet_depart):
        p = []
        p.append(sommet_depart)
        parent={}
        parent[sommet_depart] = ""

        while p != []:
            sommet_courant = p.pop(len(p)-1)
            for v in self._graphe_dict[sommet_courant]:
                if v != parent[sommet_courant]:
                    if v in parent:
                        if sommet_depart == parent[v]:
                            return True
                    else:
                        parent[v]=sommet_courant
                        p.append(v)
        return False

    def __iter__(self):
        """ on crée un itérable à partir du graphe"""
        self._iter_obj = iter(self._graphe_dict)
        return self._iter_obj

    def __next__(self):
        """ Pour itérer sur les sommets du graphe """
        return next(self._iter_obj)

    def __str__(self):
        res = "sommets: "
        for k in self._graphe_dict:
            res += str(k) + " "
        res += "\naretes: "
        for arete in self.__list_aretes():
            res += str(arete) + " "
        return res

#################################################
##                  FONCTIONS                  ##
#################################################

def construireEchiquier(d : int):
    liste = {}
    for i in range (d**2):
        liste[i]=[]
    return liste

def reineMenacee(g : Graphe, pos : int):
    menace = False
    for i in g.all_sommets():
        if pos in g._graphe_dict[i]:
            menace=True
    return menace

def placer(pos : int):
    pass

def placerReines(g : Graphe, d : int):
    pos_reine=0
    mat=[0]*(d**2)
    for i in range(d):
        pos_reine=random.randint(1,d**2)
        menacee=reineMenacee(g,pos_reine)
        while(menacee):
            pos_reine=random.randint(1,d**2)
            menacee=reineMenacee(g,pos_reine)
        mat[pos_reine-1]=1
        placer(pos_reine)
    return mat

def afficher_mat(mat : list, d : int):
    for i in range(d):
        ligne=[]
        for j in mat[i*d:(i+1)*d]:
            ligne.append(j)
        print(ligne)

#################################################
##            PROGRAMME PRINCIPAL              ##
#################################################
dim = int(input("Entrez la dimension de l'échiquier : "))
g = construireEchiquier(dim)
graphe = Graphe(g)
echiquier = placerReines(graphe,dim)
afficher_mat(echiquier,dim)