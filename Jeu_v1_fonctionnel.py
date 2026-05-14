"""
VIGROUX Naïs - VIGN90290401
MGA802-01 ETE26
Module 03 - Jeu du Pendu
"""
import random
import unicodedata
import string

"""
Cette fonction permet au joueur de fournir son propre fichier de mots en répondant "oui" exactement (sans majuscule): 
- il doit contenir seulement des mots (pas de tabulation) et ne pas être vide
- l'utilisateur doit donner le chemin d'accès de l'ordinateur vers ce fichier
- les mots peuvent contenir des accents que le code triera ensuite
Pour toute autre réponse, le code prendra le fichier de mots fourni sur Moodle
"""
def fournir_mots():
    rep=str(input("Voulez vous utiliser votre propre fichier texte ? oui ou non"))
    if rep== "oui":
        try:
            fichier=input("Insérez l'adresse complète du fichier :")
        except FileNotFoundError:
            print("Veuillez entrer une adresse valide")
    else:
        fichier="set_de_mots_moodle.txt"
    return fichier

#Cette fonction enregistre les mots du fichier fourni en paramètre dans une liste "mots" puis en choisi un aléatoirement qu'elle retourne
def selectionner_mot(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        mots=f.read().split()
    return random.choice(mots)

#Cette fonction supprime les accents du mot fourni en paramètre et retourne le mot sans accent
def supprimer_accents(mot):
    forme_nfd = unicodedata.normalize('NFD', mot)
    mot_propre = "".join(c for c in forme_nfd if unicodedata.category(c) != 'Mn')
    return mot_propre

#Cette fonction affiche le nombre de chances qu'il reste au joueur
def afficher_chances(chances):
    print(f"Il vous reste {chances} chances.")

#Cette fonction vérifie si le mot en cours d'être deviné est égal au mot à deviner et si oui indique au joueur qu'il a gagné
def gagner_partie(mot_devine):
    if "_" not in mot_devine:
        print(f"Bravo! Vous avez gagné. Le mot à deviner était {mot_complet}")
        return True
    else:
        return False

#Cette fonction affiche au joueur qu'il a perdu et le mot qu'il cherchait à deviner
def perdu_partie():
    print(f"Dommage, vous avez perdu.Le mot à deviner était {mot_complet} ")

#Cette fonction affiche une lettre non présente dans le mot à deviner ni dans celles déjà tentées par l'utilisateur
def donner_bonus():
    alphabet = string.ascii_lowercase
    lettres_absentes=[]
    for lettre in alphabet:
        if lettre not in mot_complet and lettre not in liste_lettres:
            lettres_absentes.append(lettre)
    bonus= random.choice(lettres_absentes)
    print(f"BONUS: La lettre {bonus} n'est pas dans le mot à deviner.")

#Cette fonction permet de rejouer en relançant la fonction "jouer_pendu" ou de quitter selon le souhait du joueur
def fin_de_partie():
    rep=str(input("Souhaitez-vous rejouer ? oui ou non "))
    if rep=="oui":
        jouer_pendu()
    else:
        exit()

"""Cette fonction demande au joueur d'entrer une lettre et vérifie qu'il s'agit bien d'une lettre et qu'elle est unique, 
sinon elle boucle jusqu'à avoir une lettre valide"""
def demander_lettre():
    while True:
        lettre = input("Entrez une lettre: ").lower()
        if len(lettre)!=1:
            print("Erreur: vous devez entrer une seule lettre")
        elif not   lettre.isalpha():
            print("Erreur: ce n'est pas une lettre valide")
        else:
            return lettre

"""Cette fonction vérifie si la lettre donnée par l'utilisateur se trouve dans le mot à deviner 
la variable mot_devine enregistre cette lettre à son emplacement et indique au joueur qu'il a trouvé
sinon elle indique au joueur que la lettre n'est pas dans le mot
la fonction retourne un booléen selon si la lettre devinée était dans le mot (True) ou pas (False)
Elle enregistre également les lettres données par le joueur pour que lors du bonus il affiche une lettre non essayée
"""
def verifier_dans_le_mot(mot_devine):
    reponse = False
    lettre=demander_lettre()
    liste_lettres.append(lettre)
    for i in range (len(mot_complet)):
        if lettre==mot_complet[i]:
            mot_devine[i]=lettre
            reponse=True
    if reponse:
        print("La lettre est bien dans le mot.")
    else:
        print("La lettre ne se trouve pas dans le mot.")
    return reponse


#Fonction jouer au pendu qui peut reboucler sur elle-même si le joueur souhaite rejouer :
def jouer_pendu(chances=6):
    print("Bienvenue dans le jeu du Pendu!")  # message de bienvenue
    fichier = fournir_mots()  # enregistrer le fichier de mots soit fourni par le joueur soit de base
    mot_initial = selectionner_mot(fichier)  # choisir un mot aléatoire parmi le fichier choisi
    global mot_complet
    mot_complet = supprimer_accents(mot_initial).lower()
    mot_devine = ["_"]*len(mot_complet)
    global liste_lettres
    liste_lettres = []
    afficher_chances(chances) #affiche le nombre de chances qu'il reste
    while chances > 0:
        print(mot_devine)
        rep=verifier_dans_le_mot(mot_devine)
        if not rep:
            chances-=1

        if gagner_partie(mot_devine):
            fin_de_partie()

        if chances==1:
            donner_bonus()

        afficher_chances(chances)

    if chances==0:
        perdu_partie()
        fin_de_partie()

#Lancement d'une partie de pendu
jouer_pendu()





