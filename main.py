class Table:
    def __init__(self, nom, attributs):
        self.nb_attributs = attributs
        self.nom = nom
        self.attributs = []
        for i in range(attributs):
            elt = input(f"Nom de l'attribut n°{i+1}")
            self.attributs.append(elt)
        self.nb_entree = 0
        self.entrees = [self.attributs]


    def ajouter(self, attribut): # ajoute un attribut à la fin de la table
        self.attributs.append(attribut)
        self.nb_attributs+=1
    
    def retirer(self): # retirer le dernier attribut ajouté
        self.attributs.pop()
        self.nb_attributs-=1


class List_Tables:
    def __init__(self):
        self.taille = 0
        self.liste = []
    
    def ajouter_table(self, table):
        self.taille +=1
        self.liste.append(table)

    def retirer_table(self, table):
        self.taille-=1
        self.liste.pop()

def Input_to_SQL(tableau):
    nom = input("Nom du tableau : ")
    taille = int(input("nombres d'attributs : "))
    table = Table(nom, taille)
    for i in range(taille):
        # il manque pleins de trucs en fait
        pass


def interface():
    liste_tables = List_Tables()
    IN = -1
    while not (0 < IN < 5):
        print("Que voulez vous faire :")
        print("1: info -> SQL\n2: info -> mcd...\n")
        IN = int(input("votre réponse : "))
    match IN:
        case 1:
            Input_to_SQL(liste_tables)
        case 2:
            pass
        case _:
            pass

"""

    to do list :
    - Fix table.ajouter et table.retirer
    - faire Input_to_SQL
    - faire Interface
"""

interface()
