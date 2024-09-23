#### Imports et définition des variables globales
"""
il veut une docstring, y a pas de module car pas besoin
"""


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    current_char=s[0]
    res=[]
    count=0
    for char in s:
        if char!=current_char:
            res.append((current_char,count))
            count=1  #on commence à recompter pour la prochaine lettre
            current_char=char # on passe a la lettre suivante après avoir assigné le tuple
        else:
            count+=1
    res.append((current_char,count))

    return res


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    se=set(s)
    if len(se)<=2: #on isole les dernieres comparaisons, max 2
        if len(se)==1:
            return [(s[0],1)]
        if len(se)==2:
            i=0
            while s[i]==s[i+1]:#compte le nb de l'avant derniere lettre
                i+=1
            return [(s[0],i+1),(s[i+2],len(s)-i-1)]

    if s[0]==s[1]: # cas general de la chaine, si egalité on compte combien d'occurence
        i=0
        while s[i]==s[i+1]:
            i+=1
        return [(s[0],i+1)] +artcode_r(s[i+1:])
    return [(s[0],1)]+artcode_r(s[1:])


#### Fonction principale


def main():
    """
    ne retoune rien, c'est un brouillon
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
