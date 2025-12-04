#### Imports et définition des variables globales
"""
Ce programme permet de lire des fichiers csv
"""
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename,mode="r",encoding="utf8") as f:
        lignes=list(csv.reader(f,delimiter=";"))
        for i in range(len(lignes)):
            for j in range(len(lignes[i])):
                lignes[i][j]=int(lignes[i][j])
    return lignes

def get_list_k(data, k):
    """
    Cette fonction permet de retourner une ligne de la liste principale
    """
    return data[k]

def get_first(l):
    """
    Cette fonction permet de retourner le premier élément d'une liste
    """
    return l[0]

def get_last(l):
    """
    Cette fonction permet de retourner le dernier élément d'une liste
    """
    return l[-1]

def get_max(l):
    """
    Cette fonction permet de retourner l'élément maximum d'une liste
    """
    return max(l)

def get_min(l):
    """
    Cette fonction permet de retourner l'élément minimum d'une liste
    """
    return min(l)

def get_sum(l):
    """
    Cette fonction permet de retourner la somme des éléments d'une liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
    Cette fonction permet de faire des tests
    """
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
