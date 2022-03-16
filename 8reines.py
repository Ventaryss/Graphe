# Créé par vince, le 16/03/2022 en Python 3.7

import random

class Graphe(object):
    def __init__(self, graphe_dict=None):
        if graphe_dict == None:
            graphe_dict = {}
        self._graphe_dict = graphe_dict

    def aretes(self, sommet):
        if ((sommet in self._graphe_dict)==True):
            return self._graphe_dict[sommet]
        else:
            return "Erreur, le sommet n'est pas dans le graphe"

    def all_sommets(self):
        liste_sommets=[]
        for s in (self._graphe_dict.keys()):
            liste_sommets.append(s)
        return liste_sommets

    def all_aretes(self):
        return self.__list_aretes()

    def add_sommet(self, sommet):
        if sommet not in self._graphe_dict:
            self._graphe_dict[sommet]=set()
        else:
            print("Le sommet est déjà dans le graphe")

    def add_arete(self, arete):
        if arete[0] not in self._graphe_dict or arete[1] not in self._graphe_dict:
            print("erreur, un des deux sommets n'est pas dans le graphe")
        else:
            self._graphe_dict[arete[0]].add(arete[1])
            self._graphe_dict[arete[1]].add(arete[0])


    def __list_aretes(self):
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
        return len(self._graphe_dict[sommet])

    def trouve_sommet_isole(self):
        isoles=[]
        for  i in self._graphe_dict.keys():
            if  self.sommet_degre(i)==0:
                isoles.append(i)
        return isoles

    def list_degres(self):
        degres=[]
        for i in self._graphe_dict.keys():
            degres.append(self.sommet_degre(i))
        degres.sort(reverse=True)
        return tuple(degres)

    def parcours_largeur(self, sommet_depart: str) -> list:
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
        self._iter_obj = iter(self._graphe_dict)
        return self._iter_obj

    def __next__(self):
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

def construireEchiquier():
    liste = {}
    for i in range (1,65):
        liste[i]=[]
    return liste

def reineMenacee(g : Graphe,pos : int ):
    menace = False
    for i in g.all_sommets():
        if pos in g._graphe_dict[i]:
            menace=True
    return menace

def placer(pos : int):
    pass

def placerReines(g : Graphe):
    pos_reine=0
    mat=[]
    for i in range(1,9):
        pos_reine=random.randint(1,8)
        menacee=reineMenacee(g,pos_reine)
        while(menacee):
            pos_reine=random.randint(1,8)
            menacee=reineMenacee(g,pos_reine)
        ligne=[0]*8
        ligne[pos_reine-1]=1
        mat.append(ligne)
        placer(pos_reine)
    return mat

def afficher_mat(mat : list):
    for i in mat:
        print(i)

#################################################
##            PROGRAMME PRINCIPAL              ##
#################################################

g = construireEchiquier()
graphe = Graphe(g)
echiquier = placerReines(graphe)
afficher_mat(echiquier)